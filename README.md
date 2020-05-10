# photochnaja-api
<!-- vim-markdown-toc GFM -->

* [Development](#development)
	* [Configuring application](#configuring-application)
	* [Docker containers](#docker-containers)
		* [Database](#database)
			* [Microsoft SQL Server](#microsoft-sql-server)
		* [Blob storage](#blob-storage)
			* [Azurite](#azurite)
* [Requirements](#requirements)
	* [1. Python 3.7+](#1-python-37)
	* [2. Python SQL Driver - pyodbc](#2-python-sql-driver---pyodbc)
		* [Installation](#installation)
			* [Windows](#windows)
			* [Linux (Debian)](#linux-debian)
			* [MacOS](#macos)

<!-- vim-markdown-toc -->
## Development
### Configuring application
1. To configure development environment (create virtualenv, install packages from `requirements.txt` ) run script `configure.sh` for _Unix_ systems and `configure.cmd` for _Windows_;

2. Before running application it's necessary to set variables for `flask` application in `application/setting.py`:

	__Variables:__

	+ `SECRET_KEY` - uses for session and to sign authentication token. As soon as the value of `SECRET_KEY` changes all previously created sessions become invalid. In order to generate string for `SECRET_KEY` you can use such example:

	```python
	import os
	os.urandom(24)
	```

	F.ex. `SECRET_KEY='\xb2d\xd3\xad\xbb\x84\r\xd5\xa8\xd7R\x0b\xbf\xb7\xb8\xf7\xd0SF\xabw\xfd\xa9!'`

	_Database:_

	+ `DATABASE_USER` - login of user to have access to database. F.ex. `DATABASE_USER = 'sa'`;
	+ `DATABASE_PASSWORD` - password of user to havee accees to database. F.ex. `DATABASE_PASSWORD = 'password1/'`;
	+ `DATABASE_HOST` - host name with necessary database server. F.ex. `DATABASE_HOST = 'localhost'`;
	+ `DATABASE_PORT` - port of database server. F.ex. `DATABASE_PORT = '1433'`;
	+ `DATABASE_NAME` - name of database. F.ex. `DATABASE_NAME = 'photoviewer_db'`;
	+ `DATABASE_DRIVER` - name of dirver for database. F.ex. `DATABASE_DRIVER = 'ODBC+Driver+17+for+SQL+Server'`;
	+ `SQLALCHEMY_DATABASE_URI` - union of all previous varibales in single database connection string. Value should be in `app.config['SQLALCHEMY_DATABASE_URI']`.

	_Storage_:

	+ `STORAGE_CONNECTION_STRING` - string with different parameters to connect to storage account.

	Connection string consists of _Default Endpoint Protocol_, _AccountName_, _AccountKey_, _Endpoint_ for every service (_BlobEndpoint_, _TableEndpoint_, _QueueEndpoint_).

	F.ex. for __local blob storage__ ([Azurite](#azurite)): `STORAGE_CONNECTION_STRING='DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;'`

	F.ex. for __remote blob storage__ (_Azure Blob Storage_): `STORAGE_CONNECTION_STRING='DefaultEndpointsProtocol=https;AccountName=photochnaja;AccountKey=Zi6snzZ0pzqx5Y/MoewmaaGCjCwOm6nQzqZXgJeUlv4SLKHitC2BPNW557iQ9p9+seV2gO70IzZfMlSU+B1cBw==;EndpointSuffix=core.windows.net'`

3. To run application with __development http-server__ run script `run-dev.sh` for _Unix_ systems and `run-dev.cmd` for Windows. To run application with __production http-server__ run script `run-prod.sh` only for _Unix_ systems;

### Docker containers
In order to test application locally use docker containers. Besides these docker container you can use to deploy to own server with external dependencies.

#### Database
##### Microsoft SQL Server
Microsoft SQL Server is used as database in project because application is aimed at _Microsoft Azure_.

#### Blob storage
##### Azurite
Azurite is used as blob storage in project. It's cross platform local implementation of _Azure Blob storage_.

To connect to _auzrite_ use the following command:

```sh
docker exec -it azure_storage_photochnaja sh
```

## Requirements

### 1. Python 3.7+

### 2. Python SQL Driver - pyodbc
The application use `MS SQL Server`. It's necessary to have 
`ODBC Driver 17 for SQL Server`. You can read [more](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver15).

#### Installation

##### Windows
The driver is installed when you run msodbcsql.msi from one of the
[Downloads for Windows](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15#download-for-windows).

When you invoke msodbcsql.msi, only the client components are installed by default.
The client components are files that support running an application that was
developed using the driver. To install the SDK components, specify ADDLOCAL=ALL
on the command line. Here is an example.

```cmd
msiexec /i msodbcsql.msi ADDLOCAL=ALL  
```

##### Linux (Debian)
```bash
sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

#Download appropriate package for the OS version
#Choose only ONE of the following, corresponding to your OS version

#Debian 8
curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list

#Debian 9
curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list

#Debian 10
curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

exit
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install msodbcsql17

# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc

# optional: for unixODBC development headers
sudo apt-get install unixodbc-dev

# optional: kerberos library for debian-slim distributions
sudo apt-get install libgssapi-krb5-2
```
##### MacOS
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools
```
