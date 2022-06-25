# Buld stage
FROM golang:1.16-alpine3.13 AS builder

WORKDIR /app

COPY go.mod .
COPY go.sum .

COPY service_account.json .

RUN mkdir controllers
COPY ./controllers ./controllers

RUN mkdir models
COPY ./models ./models

RUN mkdir tmp

# RUN mkdir tests
# COPY ./tests ./tests

RUN go mod download

COPY . .
RUN go build -o main main.go

# RUN go build -o ./out/dist .
#CMD ./out/dist

# Run stage
FROM alpine:3.13
WORKDIR /app

COPY service_account.json .

COPY --from=builder /app/main .

EXPOSE 8080

CMD ["/app/main"]



