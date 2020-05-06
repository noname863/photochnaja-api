from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, jsonify
from flask_cors import cross_origin
from sqlalchemy import or_

from application import app, db
from application.models import User


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = User.query.filter_by(login=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(
                expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


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
