package main

import (
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/pkg/errors"
)

const (
	// Chosen by fair dice roll, guarenteed to be random.
	// We don't really care about this being configurable
	// or even want it to be different across restarts so
	// it's just a constant.
	jwtSecret = "1f0bc2c3-30a8-48c8-b830-bf486f7e14ba"
)

type claims struct {
	jwt.StandardClaims
	IsAdmin bool `json:"bsides_is_admin"`
}

func newToken(username string, admin bool) (string, error) {
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, &claims{
		StandardClaims: jwt.StandardClaims{
			Subject:   username,
			ExpiresAt: time.Now().Add(tokenDuration).Unix(),
		},
		IsAdmin: admin,
	})

	ss, err := token.SignedString([]byte(jwtSecret))
	return ss, errors.Wrap(err, "unable to sign token")
}

func parseValidateToken(rawToken string) (*claims, error) {
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
		return nil, errors.New("invalid token")
	}

	claims, ok := token.Claims.(*claims)
	if !ok {
		return nil, errors.New("got incorrect type for claims")
	}

	return claims, nil
}
