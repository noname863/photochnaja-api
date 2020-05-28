#!/bin/bash

source azure.conf

# Configure start command for api appservice
echo -e "\n-----Configuring appservice (set startup):"
az webapp config set \
  --name $m_api \
  --resource-group $m_group \
  --startup-file $m_api_startup_file
