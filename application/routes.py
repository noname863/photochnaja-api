from datetime import datetime, timedelta

import jwt
from flask import request, jsonify
from flask_cors import cross_origin
from sqlalchemy import or_

from application import app, db
from application.models import User


@app.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    data = request.get_json()
    if User.query.filter(or_(User.email == data['email'],
                             User.login == data['login'])).first():
        return jsonify(
            {'message': 'User with the same email or login is existed.'}), 209

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user.jsonify(), 201


@app.route('/signin', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify(
            {'message': 'Invalid credentials', 'authenticated': False}), 401

    token = jwt.encode({
        'sub': user.login,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})
