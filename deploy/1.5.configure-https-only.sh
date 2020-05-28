#!/bin/bash

source azure.conf

# Update httpsOnly for api appservice
echo -e "\n-----Configuring https for appservice (httpsOnly):"
az webapp update \
  --name $m_api \
  --resource-group $m_group \
  --set httpsOnly=true
