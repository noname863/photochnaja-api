#!/bin/bash

source azure.conf

# Get database
echo "-----Getting database:"
az sql db show \
  --resource-group $m_group \
  --name $m_api_database \
  --server $m_api_db_server
