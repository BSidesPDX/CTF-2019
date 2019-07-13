FROM node:current-alpine AS builder

ARG API_URL
RUN if [ "$API_URL" = "" ]; then echo "API_URL needs to be set"; exit 1; fi

WORKDIR /src

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine

COPY --from=builder /src/build /usr/share/nginx/html
COPY --from=builder /src/nginx.conf /etc/nginx/conf.d/default.conf