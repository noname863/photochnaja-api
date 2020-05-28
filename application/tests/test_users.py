import json
import unittest

import sqlalchemy

from application import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = app.config['TEST_DATABASE_URI']


class BasicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with sqlalchemy.create_engine(
                app.config['INITIAL_DATABASE_URI'],
                isolation_level='AUTOCOMMIT'
        ).connect() as connection:
            connection.execute(
                'CREATE DATABASE ' + app.config['TEST_DATABASE_NAME'])

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        db.drop_all()

    def test_user_signup(self):
        with app.app_context():
            user_map = {'email': 'test@mail.ru',
                        'login': 'test_login',
                        'password': 'test_password'}
            response = self.app.post('/signup',
                                     data=json.dumps(user_map),
                                     content_type='application/json')
            self.assertEqual(response.status_code, 201)
            response_user = json.loads(response.get_data(as_text=True))
            self.assertEqual(response_user['email'], user_map['email'])
            self.assertEqual(response_user['login'], user_map['login'])

    def test_user_signin(self):
        with app.app_context():
            user_map = {'email': 'test@mail.ru',
                        'login': 'test_login',
                        'password': 'test_password'}
            self.app.post('/signup',
                          data=json.dumps(user_map),
                          content_type='application/json')

            response = self.app.post('/signin',
                                     data=json.dumps(
                                         {'login': user_map['login'],
                                          'password': user_map['password']}),
                                     content_type='application/json')

            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(
                json.loads(response.get_data(as_text=True))['token'])


if __name__ == "__main__":
    unittest.main()
