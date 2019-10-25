FROM node:current-alpine AS builder

WORKDIR /src

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN adduser --disabled-password --gecos '' web300secbackend
USER web300secbackend
ENTRYPOINT [ "node", "index.js"]