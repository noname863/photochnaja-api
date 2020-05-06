from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)
app.config.from_pyfile('settings.py')
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)

from application import routes
