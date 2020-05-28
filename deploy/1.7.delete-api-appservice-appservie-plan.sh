#!/bin/bash

source azure.conf

# Delete appservice for api
echo "Deleting appservice..."
az resource delete \
  --name $m_api \
  --resource-group $m_group \
  --resource-type "Microsoft.Web/sites"

# Delete appservice plan for api
echo "Deleting appservice plan..."
az resource delete \
  --name $m_api_plan \
  --resource-group $m_group \
  --resource-type "Microsoft.Web/serverFarms"

eval $post_command_delete_api
