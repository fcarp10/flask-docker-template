# flask-docker-template

A template of a lightweight dockerized flask app using as base image `python:3.7.9-alpine`

## Requirements

- Docker >= 19.03

## Build and run with Docker

Build and push with docker (example):

    docker build -t fcarp10/flask-docker-template:latest .
    docker push fcarp10/flask-docker-template:latest

Run the container: 

    docker run -p 5000:5000 fcarp10/flask-docker-template:latest

Check if running correctly on `http://localhost:5000`.


### (Optional) Multi-arch building with experimental `docker buildx`.

Temporal configurations until `buildx` final version is released:

    export DOCKER_CLI_EXPERIMENTAL=enabled
    docker buildx create --use

Build and push multi-arch images (example):

    docker buildx build --push --platform linux/arm64/v8,linux/amd64 --tag fcarp10/flask-docker-template:latest .


