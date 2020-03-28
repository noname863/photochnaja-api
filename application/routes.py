from flask_cors import cross_origin

from application import app

from flask import json


@app.route('/', methods=['GET'])
@cross_origin()
def hello():
    return json.dumps({'message': "Backend message."})
