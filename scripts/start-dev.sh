#!/bin/bash

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8080}

uvicorn app.main:app --reload --proxy-headers --host $HOST --port $PORT
