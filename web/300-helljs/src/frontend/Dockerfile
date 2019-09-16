FROM node:current-alpine AS builder

WORKDIR /src

COPY package.json package-lock.json ./

RUN npm install

COPY . .

ARG VULNERABLE_API_URL
RUN if [ "$VULNERABLE_API_URL" = "" ]; then echo "VULNERABLE_API_URL needs to be set"; exit 1; fi

ARG SECURE_API_URL
RUN if [ "$SECURE_API_URL" = "" ]; then echo "SECURE_API_URL needs to be set"; exit 1; fi

RUN npm run build

FROM nginx:stable-alpine

COPY --from=builder /src/dist /usr/share/nginx/html
COPY --from=builder /src/nginx.conf /etc/nginx/conf.d/default.conf