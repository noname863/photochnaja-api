#!/bin/bash

REPO_URL='repo_url'
AUTH_TOKEN='github_auth_token'

curl --location --request POST "$REPO_URL/dispatches" \
  --header "Authorization: Bearer $AUTH_TOKEN" \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "event_type": "start-azure-request-workflow"
}'
