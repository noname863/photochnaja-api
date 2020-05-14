#!/bin/bash

source azure.conf

# Delete slot of api appservice
echo "-----Deleting deployment slot..."
az webapp deployment slot delete \
  --name $m_api \
  --resource-group $m_group \
  --slot $m_api_slot
