#!/bin/bash

source azure.conf

# Swap slot of api appservice
echo "-----Swapping deployment slot..."
az webapp deployment slot swap \
  --name $m_api \
  --resource-group $m_group \
  --slot $m_api_slot
