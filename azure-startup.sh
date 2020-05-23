# Install dependencies for 'pyodbc' python package
apt update
apt install g++ -y
apt install unixodbc-dev -y
apt install unixodbc -y
apt install libodbc1 -y

# Install python packages as application dependencies
pip install -r requirements.txt

# Create table 'users' in database of application
ACCEPT_EULA=Y && apt install mssql-tools -y
/opt/mssql-tools/bin/sqlcmd \
  -S $DATABASE_HOST \
  -d photochnaja_db \
  -U $DATABASE_USER \
  -P $DATABASE_PASSWORD \
  -I \
  -i sql/3_create_tables.sql

# Startup of application
gunicorn --bind=0.0.0.0 --timeout 600 photochnaja:app
