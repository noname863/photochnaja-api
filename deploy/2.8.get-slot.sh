#!/bin/bash

source azure.conf

# Get configuration of api slot
echo "-----Getting deployment slot (source):"
az webapp deployment source show \
  --name $m_api \
  --resource-group $m_group \
  --slot $m_api_slot
