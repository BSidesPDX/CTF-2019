package main

import (
	"encoding/json"
	"net/http"
	"time"

	"github.com/fharding1/ctf/100/db"
	"github.com/sirupsen/logrus"
	"golang.org/x/crypto/bcrypt"
)

type UserCreator interface {
	CreateUser(username, hashedPassword string) error
}

type Users struct {
	UserCreator UserCreator
	Logger      *logrus.Logger
}

type userRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

func (ur userRequest) Validate() map[string]string {
	errs := make(map[string]string)
	if ur.Username == "" {
		errs["username"] = "should not be empty"
	}
	if ur.Password == "" {
		errs["password"] = "should not be empty"
	}
	return errs
}

func (u *Users) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, http.StatusText(http.StatusMethodNotAllowed), http.StatusMethodNotAllowed)
		return
	}

	var requestBody userRequest

	if err := json.NewDecoder(r.Body).Decode(&requestBody); err != nil {
		http.Error(w, http.StatusText(http.StatusUnprocessableEntity), http.StatusUnprocessableEntity)
		return
	}

	if warnings := requestBody.Validate(); len(warnings) != 0 {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusUnprocessableEntity)
		json.NewEncoder(w).Encode(warnings)
		return
	}

	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(requestBody.Password), bcrypt.DefaultCost)
	if err != nil {
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	err = u.UserCreator.CreateUser(requestBody.Username, string(hashedPassword))
	if exister, ok := err.(db.Exister); ok && exister.Exists() {
		http.Error(w, http.StatusText(http.StatusConflict), http.StatusConflict)
		return
	} else if err != nil {
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	u.Logger.WithField("username", requestBody.Username).Info("created user")
	w.WriteHeader(http.StatusCreated)
}

type UserFetcher interface {
	GetUser(username string) (string, error)
}

type Token struct {
	UserFetcher UserFetcher
	Logger      *logrus.Logger
}

const (
	tokenDuration = time.Hour
)

func (t *Token) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, http.StatusText(http.StatusMethodNotAllowed), http.StatusMethodNotAllowed)
		return
	}

	var requestBody userRequest

	if err := json.NewDecoder(r.Body).Decode(&requestBody); err != nil {
		http.Error(w, http.StatusText(http.StatusUnprocessableEntity), http.StatusUnprocessableEntity)
		return
	}

	if warnings := requestBody.Validate(); len(warnings) != 0 {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusUnprocessableEntity)
		json.NewEncoder(w).Encode(warnings)
		return
	}

	hashedPassword, err := t.UserFetcher.GetUser(requestBody.Username)
	if exister, ok := err.(db.Exister); ok && !exister.Exists() {
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
		return
	} else if err != nil {
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	err = bcrypt.CompareHashAndPassword([]byte(hashedPassword), []byte(requestBody.Password))
	if err == bcrypt.ErrMismatchedHashAndPassword {
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
		return
	} else if err != nil {
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	ss, err := newToken(requestBody.Username, false)
	if err != nil {
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	t.Logger.WithField("username", requestBody.Username).Info("signed JWT for user")

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"jwt": ss})
}
