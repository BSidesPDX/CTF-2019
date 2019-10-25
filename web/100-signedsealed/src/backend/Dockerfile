FROM golang:1.12-alpine AS builder

RUN apk add git

RUN adduser --disabled-password --gecos '' web100backend

WORKDIR /src/100

COPY go.mod go.sum ./
RUN go mod download

ENV CGO_ENABLED 0

COPY . .

RUN go build -o /src/100/100 /src/100/*.go

FROM scratch

# Import the user and group files from the builder.
COPY --from=builder /etc/passwd /etc/passwd

COPY --from=builder /src/100/100 /100

USER web100backend

ENTRYPOINT ["/100"]