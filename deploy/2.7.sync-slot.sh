#!/bin/bash

source azure.conf

# Swap slot of api appservice
echo "-----Syncing deployment slot..."
az webapp deployment source sync \
  --name $m_api \
  --resource-group $m_group \
  --slot $m_api_slot
