#!/bin/bash

source azure.conf

# Create a new slot
echo "-----Creating new deployment slot:"
az webapp deployment slot create \
	--name $m_api \
	--resource-group $m_group \
	--slot $m_api_slot
