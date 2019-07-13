package main

import (
	"net/http"
	"os"
	"strconv"

	"github.com/fharding1/ctf/100/db"
	"github.com/sirupsen/logrus"
)

func main() {
	// setup and configure the logger

	logger := logrus.New()

	if logJSON, _ := strconv.ParseBool(os.Getenv("LOG_JSON")); logJSON {
		logger.SetFormatter(&logrus.JSONFormatter{})
	}

	logLevel, _ := logrus.ParseLevel(os.Getenv("LOG_LEVEL"))
	logger.SetLevel(logLevel)

	// setup and configure boltdb

	db, err := db.Open(os.Getenv("DB_PATH"), 0666)
	if err != nil {
		logger.Fatal(err)
	}
	defer db.Close()

	// setup handlers

	app := &App{
		Users: &Users{UserCreator: db, Logger: logger},
		Token: &Token{UserFetcher: db, Logger: logger},
		Flag:  &Flag{Logger: logger, Flag: os.Getenv("FLAG")},
	}

	cors := &CORSMiddleware{
		Next:           app,
		AllowedOrigin:  "*",
		AllowedHeaders: []string{"Authorization"},
		AllowedMethods: []string{http.MethodGet, http.MethodPost},
	}

	log := &LogMiddleware{
		Next:   cors,
		Logger: logger,
	}

	http.ListenAndServe(":8080", log)
}
