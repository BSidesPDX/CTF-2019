package main

import (
	"net/http"
	"time"

	"github.com/sirupsen/logrus"
)

// LogMiddleware logs some information before and after requests.
type LogMiddleware struct {
	Next   http.Handler
	Logger *logrus.Logger
}

func (l *LogMiddleware) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	l.Logger.WithFields(logrus.Fields{
		"url":        r.URL.String(),
		"method":     r.Method,
		"proto":      r.Proto,
		"remoteAddr": r.RemoteAddr,
		"host":       r.Host,
	}).Info("started request")

	start := time.Now()
	l.Next.ServeHTTP(w, r)
	end := time.Now()

	l.Logger.WithFields(logrus.Fields{
		"url":        r.URL.String(),
		"method":     r.Method,
		"proto":      r.Proto,
		"remoteAddr": r.RemoteAddr,
		"host":       r.Host,
		"took":       end.Sub(start),
	}).Info("finished request")
}

// CORSMiddleware sets CORS headers and intercepts OPTIONS requests.
type CORSMiddleware struct {
	Next           http.Handler
	AllowedOrigin  string
	AllowedHeaders []string
	AllowedMethods []string
}

func (c *CORSMiddleware) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", c.AllowedOrigin)
	for _, header := range c.AllowedHeaders {
		w.Header().Add("Access-Control-Allow-Headers", header)
	}
	for _, method := range c.AllowedMethods {
		w.Header().Add("Access-Control-Allow-Methods", method)
	}

	if r.Method == http.MethodOptions {
		return
	}

	c.Next.ServeHTTP(w, r)
}
