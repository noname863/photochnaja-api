#!/bin/bash

source azure.conf

# Create Azure SQL Server
echo -e "\n-----Creating Azure SQL Server:"
az sql server create \
  --name $m_api_db_server \
  --resource-group $m_group \
  --location $m_location \
  --admin-user $m_api_db_login \
  --admin-password $m_api_db_password
