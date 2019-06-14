package main

import (
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/gorilla/mux"
	"github.com/rs/cors"
	"github.com/sirupsen/logrus"
	"golang.org/x/crypto/bcrypt"
)

const (
	jwtSecret = "1f0bc2c3-30a8-48c8-b830-bf486f7e14ba" // chosen by fair dice roll, guarenteed to be random
	flag      = "BSidesPDX{5f0505ea-72d1-40c4-8451-d4a3e19e7491}"
)

var (
	users  = make(map[string][]byte)
	logger = logrus.New()
)

func main() {
	if logJSON, _ := strconv.ParseBool(os.Getenv("LOG_JSON")); logJSON {
		logger.SetFormatter(&logrus.JSONFormatter{})
	}

	logLevel, _ := logrus.ParseLevel(os.Getenv("LOG_LEVEL"))
	logger.SetLevel(logLevel)

	router := mux.NewRouter()

	router.HandleFunc("/", swaggerHandler).Methods("GET")

	router.HandleFunc("/flag", flagHandler).Methods("GET")
	router.HandleFunc("/authenticate", authenticateHandler).Methods("POST")
	router.HandleFunc("/users", createUserHandler).Methods("POST")
	router.HandleFunc("/users/{userId}", func(w http.ResponseWriter, r *http.Request) {
		http.Error(w, http.StatusText(http.StatusNotImplemented), http.StatusNotImplemented)
	}).Methods("GET")

	c := cors.New(cors.Options{
		AllowedOrigins: []string{"*"},
		AllowedMethods: []string{"GET", "POST"},
		AllowedHeaders: []string{"Authorization"},
	})

	http.ListenAndServe(":8080", logMiddleware(c.Handler(router)))
}

func logMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		logger.WithFields(logrus.Fields{
			"url":        r.URL.String(),
			"method":     r.Method,
			"proto":      r.Proto,
			"remoteAddr": r.RemoteAddr,
			"host":       r.Host,
		}).Info("started request")

		start := time.Now()
		next.ServeHTTP(w, r)
		end := time.Now()

		logger.WithFields(logrus.Fields{
			"url":        r.URL.String(),
			"method":     r.Method,
			"proto":      r.Proto,
			"remoteAddr": r.RemoteAddr,
			"host":       r.Host,
			"took":       end.Sub(start),
		}).Info("finished request")
	})
}

type userRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

type claims struct {
	jwt.StandardClaims
	IsAdmin bool `json:"bsides_is_admin"`
}

func swaggerHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-yaml")
	io.WriteString(w, swagger)
}

func createUserHandler(w http.ResponseWriter, r *http.Request) {
	var requestBody userRequest

	if err := json.NewDecoder(r.Body).Decode(&requestBody); err != nil {
		http.Error(w, http.StatusText(http.StatusUnprocessableEntity), http.StatusUnprocessableEntity)
		return
	}

	if _, ok := users[requestBody.Username]; ok {
		http.Error(w, http.StatusText(http.StatusConflict), http.StatusConflict)
		return
	}

	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(requestBody.Password), bcrypt.DefaultCost)
	if err != nil {
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	users[requestBody.Username] = hashedPassword
	logger.WithField("username", requestBody.Username).Info("created user")

	w.Header().Set("Location", "/users/"+requestBody.Username)
	w.WriteHeader(http.StatusCreated)
}

func authenticateHandler(w http.ResponseWriter, r *http.Request) {
	var requestBody userRequest

	if err := json.NewDecoder(r.Body).Decode(&requestBody); err != nil {
		http.Error(w, http.StatusText(http.StatusUnprocessableEntity), http.StatusUnprocessableEntity)
		return
	}

	hashedPassword, ok := users[requestBody.Username]
	if !ok {
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
		return
	}

	if err := bcrypt.CompareHashAndPassword(hashedPassword, []byte(requestBody.Password)); err != nil {
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
		return
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, &claims{
		StandardClaims: jwt.StandardClaims{
			Subject:   requestBody.Username,
			ExpiresAt: time.Now().Add(time.Hour).Unix(),
		},
		IsAdmin: false,
	})

	ss, err := token.SignedString([]byte(jwtSecret))
	if err != nil {
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		return
	}

	logger.WithField("username", requestBody.Username).Info("signed JWT for user")
	json.NewEncoder(w).Encode(map[string]string{"jwt": ss})
}

func flagHandler(w http.ResponseWriter, r *http.Request) {
	rawToken := strings.TrimPrefix(r.Header.Get("Authorization"), "Bearer ")

	token, err := jwt.ParseWithClaims(rawToken, &claims{}, func(token *jwt.Token) (interface{}, error) {
		// allow "none" signature type
		if token.Method == jwt.SigningMethodNone {
			return jwt.UnsafeAllowNoneSignatureType, nil
		} else if token.Method != jwt.SigningMethodHS256 {
			return nil, errors.New("unexpected signature type")
		}

		return []byte(jwtSecret), nil
	})

	if err != nil || !token.Valid {
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
		return
	}

	claims, ok := token.Claims.(*claims)
	if !ok {
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
		return
	}

	if !claims.IsAdmin {
		http.Error(w, http.StatusText(http.StatusForbidden), http.StatusForbidden)
		return
	}

	logger.WithField("username", claims.Subject).Info("returned the flag")
	json.NewEncoder(w).Encode(map[string]string{"flag": flag})
}
