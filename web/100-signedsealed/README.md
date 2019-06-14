# 100 - Signed, Sealed, Delivered, I'm Yours!

## Description

This challenge is a pretty simple JWT "none" algorithm challenge. You craft a "none" algorithm JWT and change the admin claim to true to get the flag.

The challenger will only be given the address of the frontend.

## Deploy

The backend has the following environment variables:
* LOG_JSON - log as JSON instead of plaintext
* LOG_LEVEL - minimum log level to log at (probably should be "trace")

The frontend Dockerfile has the following build arguments:
* API_URL - external address of the backend

## Challenge

Implementing your own authorization is usually a bad idea, but not if you're a rockstar dev like me.

Flag: `BSidesPDX{5f0505ea-72d1-40c4-8451-d4a3e19e7491}`

## Solve Steps

You could do all of this via the API (especially since it has an "accidentally" exposed swagger doc) or just by using the frontend.

### Register/Login

Register an account and login.

### Attempt to get the flag

Try to get the flag, notice you get a 401 Unauthorized. Inspect the request
and grab the JWT from the Authorization header.

### Inspect JWT

Visit jwt.io and paste in the JWT.
Note the `bsides_is_admin` claim in the payload and the HS256 alg in the header.

### Craft and store the JWT

```js
const tok = localStorage.getItem('jwt')
  .split('.')
  .slice(0, 2)
  .map(v => JSON.parse(atob(v)))
tok[0].alg = "none"
tok[1].bsides_is_admin = true
localStorage.setItem('jwt', tok.map(v => btoa(JSON.stringify(v))).join(".") + ".")
```

### Get the flag

Hit "Get flag"!