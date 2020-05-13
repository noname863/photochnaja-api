import json
import unittest

from application import app, db

TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        print(app.config['SQLALCHEMY_DATABASE_URI'])
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        db.drop_all()

    ###############
    #### tests ####
    ###############

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
            if __name__ == "__main__":
                unittest.main()

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
