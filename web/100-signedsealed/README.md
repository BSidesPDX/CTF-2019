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

web100.bsidespdxctf.party:48323

Flag: `BSidesPDX{5f0505ea-72d1-40c4-8451-d4a3e19e7491}`