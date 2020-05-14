#!/bin/bash

source azure.conf

# Delete database from SQL server
echo "Deleting database..."
az sql db delete \
  --resource-group $m_group \
  --name $m_api_database \
  --server $m_api_db_server \
  --yes

# Delete SQL server
echo "Deleting sql server..."
az sql server delete \
  --resource-group $m_group \
  --name $m_api_db_server \
  --yes
