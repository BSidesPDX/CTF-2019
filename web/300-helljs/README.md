# 300 - Hell.js

## Description

This challenge involves MongoDB injection, Server-Side Javascript Injection, and crafting JWTs.

The challenger will only be given the address of the frontend.

## Deploy

The frontend requires the following environment variables:

* VULNERABLE_API_URL - public URL of the vulnerable API
* SECURE_API_URL - public URL of the secure API

And will listen on port 8080.

The vulnerable backend requires the following environment variables:

* JWT_SECRET - secret used to sign the JWTs (should be a random UUID), **MUST** be the same for the secure backend
*  MONGODB_URL - MongoDB URL (e.g. `mongodb://localhost:27017`)
*  MONGODB_DB_NAME - MongoDB Database Name (can be anything)
*  PORT - port to listen on

The secure backend requires the following environment variables:

* JWT_SECRET - secret used to sign the JWTs (should be a random UUID), **MUST** be the same for the vulnerable backend
*  PORT - port to listen on

## Challenge

Minimum Viable Security

web300.bsidespdxctf.party:27330

Flag: `BSidesPDX{7h3_f8_0f_my_4pp_r3575_w17h_l3f7-p4d?_cb017f1f}`