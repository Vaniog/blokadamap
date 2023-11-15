#!/bin/bash

DOCKER_NAME=${DOCKER_NAME:-fastapi_app}

docker build -t "$DOCKER_NAME" .
