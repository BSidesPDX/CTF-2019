FROM golang:1.13-alpine AS builder

RUN apk add git

WORKDIR /src/200

COPY go.mod go.sum ./
RUN go mod download

ENV CGO_ENABLED 0

COPY . .

RUN go build -o /src/200/200 /src/200/*.go

FROM scratch

COPY --from=builder /src/200/200 /200

ENTRYPOINT ["/200"]