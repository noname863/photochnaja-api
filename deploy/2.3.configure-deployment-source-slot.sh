#!/bin/bash

source azure.conf

# Configure deployment source
echo -e "\n-----Configuring deployment source for slot (repo + branch + manual-integration):"
az webapp deployment source config \
  --name $m_api \
  --resource-group $m_group \
  --manual-integration \
  --repo-url $m_api_repo \
  --branch $m_api_slot_branch \
  --slot $m_api_slot
