#!/bin/bash

source azure.conf

# Configure firewall for local host
echo -e "\n-----Configuring firewall for local host:"
az sql server firewall-rule create \
  --resource-group $m_group \
  --server $m_api_db_server \
  --name AllowMyIP \
  --start-ip-address $m_public_ip \
  --end-ip-address $m_public_ip
