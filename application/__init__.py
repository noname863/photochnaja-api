from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config.from_pyfile('settings.py')
app.config['CORS_HEADERS'] = 'Content-Type'

from application import routes
