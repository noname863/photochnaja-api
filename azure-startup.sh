# Install dependencies for 'pyodbc' python package
apt update
apt install g++ -y
apt install unixodbc-dev -y
apt install unixodbc -y
apt install libodbc1 -y

# Install python packages as application dependencies
pip install -r requirements.txt

# Startup of application
gunicorn --bind=0.0.0.0 --timeout 600 photochnaja:app
