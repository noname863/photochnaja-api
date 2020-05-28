#!/bin/bash

source azure.conf

# Configure start command
echo -e "\n-----Configuring deployment slot (set startup):"
az webapp config set \
  --name $m_api \
  --resource-group $m_group \
  --startup-file $m_api_startup_file \
  --slot $m_api_slot
