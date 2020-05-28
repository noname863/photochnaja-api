#!/bin/bash

source azure.conf

# Create database on Azure SQL Server
echo -e "\n-----Creating database on Azure SQL Server:"
az sql db create \
  --resource-group $m_group \
  --server $m_api_db_server \
  --name $m_api_database \
  --edition Basic \
  --service-objective Basic \
  --capacity 5 \
  --zone-redundant false
