# Install python packages as application dependencies
pip install -r requirements.txt

# Startup of application
gunicorn --bind=0.0.0.0 --timeout 600 photochnaja:app