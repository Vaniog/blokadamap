#!/bin/bash
curl -X "PUT" \
  "http://localhost:8080/records/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
  "data": "string"
}'
