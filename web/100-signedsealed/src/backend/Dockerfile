FROM golang:1.12-alpine AS builder

RUN apk add git

WORKDIR /src/100

COPY go.mod go.sum ./
RUN go mod download

ENV CGO_ENABLED 0

COPY . .

RUN go build -o /src/100/100 /src/100/*.go

FROM scratch

COPY --from=builder /src/100/100 /100

ENTRYPOINT ["/100"]