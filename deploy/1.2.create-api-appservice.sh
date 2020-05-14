#!/bin/bash

source azure.conf

# Create a appservice for api
echo -e "\n-----Creating appservice:"
az webapp create \
  --name $m_api \
  --resource-group $m_group \
  --plan $m_api_plan \
  --runtime $m_api_runtime
