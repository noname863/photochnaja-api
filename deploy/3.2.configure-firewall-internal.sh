#!/bin/bash

source azure.conf

# Configure firewall for internal services
echo -e "\n-----Configuring firewall for internal services:"
az sql server firewall-rule create \
  --resource-group $m_group \
  --server $m_api_db_server \
  --name AllowInternalIP \
  --start-ip-address $m_api_db_start_ip \
  --end-ip-address $m_api_db_end_ip
