# 200 - Yours truly

## Description

This challenge involves reading swagger docs and using SSRF to gain access to an
object in minio.

The challenger will only be given the address of the OpenAPI doc.

## Deploy

Minio or some S3 compatible object store must be setup and accessible to the internet
and the backend pod from the same address (so presigned URLs work). If you're using minio
I made it so it will build the files into the image, otherwise just load everything from
the web/200-yourstruly/minio/data/suspects folder into a bucket called suspects and point
the backend at that.

The "store" service should not be publicly accessible (only to the backend), and
requires: no configuration otherwise. It listens on port 8080.

The "backend" service requires the following environment variables:

* CHARACTER_SERVICE_URL - URL of the store service
* MINIO_ENDPOINT - object storage public address (not fully qualified, example: "localhost:9000")
* MINIO_ACCESS_KEY_ID - object storage access key id
* MINIO_SECRET_ACCESS_KEY - object storage secret access key

And listens on port 8081.

If you use the minio image it requires:

* MINIO_ACCESS_KEY - object storage access key id to setup
* MINIO_SECRET_ACCESS_KEY - object storage secret access key to setup

It listens on port 9000.

## Challenge

My bugs are self documenting.

web200.bsidespdxctf.party:8081/openapi.yaml

Flag: `BSidesPDX{m1cr053rv1c35-m1cr0-p41n-1n-7h3-455-9f9b6761}`