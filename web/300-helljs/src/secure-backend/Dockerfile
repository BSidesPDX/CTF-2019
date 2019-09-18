FROM node:current-alpine AS builder

WORKDIR /src

COPY package.json package-lock.json ./

RUN npm install

COPY . .

ENTRYPOINT [ "node", "index.js"]