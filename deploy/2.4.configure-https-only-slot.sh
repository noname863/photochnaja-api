#!/bin/bash

source azure.conf

# Update httpsOnly
echo -e "\n-----Configuring https (httpsOnly):"
az webapp update \
  --name $m_api \
  --resource-group $m_group \
  --set httpsOnly=true \
  --slot $m_api_slot
