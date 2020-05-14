#!/bin/bash

source 0.0.create-resource-group.sh
source 3.1.create-azure-sql-database.sh
source 3.2.configure-firewall-internal.sh
source 3.3.configure-firewall-localhost.sh
source 3.4.create-database.sh
