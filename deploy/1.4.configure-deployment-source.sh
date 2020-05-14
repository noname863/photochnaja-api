#!/bin/bash

source azure.conf

# Configure deployment source for api appservice
echo -e "\n-----Configuring deployment source for appservice (repo + branch + manual-integration):"
az webapp deployment source config \
  --name $m_api \
  --resource-group $m_group \
  --manual-integration \
  --repo-url $m_api_repo \
  --branch $m_api_branch
