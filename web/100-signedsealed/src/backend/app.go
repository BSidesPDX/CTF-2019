package main

import (
	"net/http"
	"path"
	"strings"
)

type App struct {
	Flag  http.Handler
	Token http.Handler
	Users http.Handler
}

func (a *App) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	var head string
	head, r.URL.Path = shiftPath(r.URL.Path)

	switch head {
	case "flag":
		a.Flag.ServeHTTP(w, r)
	case "token":
		a.Token.ServeHTTP(w, r)
	case "users":
		a.Users.ServeHTTP(w, r)
	default:
		http.Error(w, http.StatusText(http.StatusNotFound), http.StatusNotFound)
	}
}

func shiftPath(p string) (head, tail string) {
	p = path.Clean("/" + p)
	i := strings.Index(p[1:], "/") + 1
	if i <= 0 {
		return p[1:], "/"
	}
	return p[1:i], p[i:]
}
