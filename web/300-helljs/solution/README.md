# Solution

## Attempt to Login

Any attempts to login will be unfruitful. However, after looking at the network requests,
you'll notice that the backend is responding with `X-Powered-By: Express`, which tells you
the backend is probably Node with Express. Knowing that a common database to use with Node
(and that the challenge is named Hell.js) you think the database might be MongoDB.

## MongoDB Injection

In your browser you click on the login request, hit Edit and Resend, and change the request
body to:

```json
{"username":{"$gt":""},"password":{"$gt":""}}
```

You get a token!

## Set in localStorage

Knowing that it's common for JWTs to be stored in localStorage, you view the app.js bundle and
search for localStorage. You find `window.localStorage.getItem('token')`, which tells you where
to put this token, so you set the token in devtools:

```javascript
window.localStorage.setItem("token", token)
```

## Customers Page

After setting your token, you notice that the login page isn't redirecting you anywhere. It seems
that it's supposed to send you somewhere after clicking the button. You search the bundle for
`routes` and see two: `/` (login page), and `/customers`. You go to the `/customers` page and are
greeted with a table of customers.

## SSJSi

The customers filter text box is clearly just normal Javascript, seeing as it's default is
`return true;` which returns all users. It looks like the input in this textbox is being submitted
to the backend via the `filter` query parameter and being parsed as a function and then being used
to `.filter()` customers. To test this, you try:

```javascript
customer.gender = JSON.stringify(process.env); return true;
```

Which gives you a `JWT_SECRET`.

## The Other Backend

You notice the customers page is making a request to a different backend's `/flag` endpoint with
the same token, but it's respoding with a 403 Forbidden. You inspect your token in jwt.io and
observe that your `get_flag` claim is set to `false`. You try setting algorithm to none like you
did in the 100, but with no success. At this point you realize you can just sign your own JWT using
the JWT_SECRET you exfiltrated, so you open up a `node` REPL after `npm install jsonwebtoken`-ing,
and run the following commands to sign a token with `get_flag` set to true:

```
> const jwt = require("jsonwebtoken");
> jwt.sign({"get_flag":true}, 'token');
```

## Getting the Flag

You submit this token to the other backend's `/flag` endpoint, and a flag is returned.