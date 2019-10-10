FROM golang:1.13-alpine AS builder

WORKDIR /src/300

ENV CGO_ENABLED 0

COPY . .

RUN go build -o /src/300/300 /src/300/main.go

FROM scratch

COPY --from=builder /src/300/300 /300

ENTRYPOINT ["/300"]