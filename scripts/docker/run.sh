#!/bin/bash

DOCKER_NAME=${DOCKER_NAME:-fastapi_app}
DOCKER_PORT=${DOCKER_PORT:-80}

docker run -d --name "$DOCKER_NAME" --network=host -p "$DOCKER_PORT":"$DOCKER_PORT" "$DOCKER_NAME"
