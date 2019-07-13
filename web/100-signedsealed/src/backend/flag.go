package main

import (
	"encoding/json"
	"net/http"
	"strings"

	"github.com/sirupsen/logrus"
)

// Flag is a handler for returning the flag given the proper authorization.
type Flag struct {
	Logger *logrus.Logger

	Flag string
}

func (f Flag) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, http.StatusText(http.StatusMethodNotAllowed), http.StatusMethodNotAllowed)
		return
	}

	rawToken := strings.TrimPrefix(r.Header.Get("Authorization"), "Bearer ")

	claims, err := parseValidateToken(rawToken)
	if err != nil {
		http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
		return
	}

	if !claims.IsAdmin {
		http.Error(w, http.StatusText(http.StatusForbidden), http.StatusForbidden)
		return
	}

	f.Logger.WithField("username", claims.Subject).Info("returned the flag")

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"flag": f.Flag})
}
