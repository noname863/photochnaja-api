from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True, nullable=False)

    def __init__(self, login, password, email):
        self.login = login
        self.password = generate_password_hash(password, method='sha256')
        self.email = email

    @classmethod
    def authenticate(cls, **kwargs):
        login = kwargs.get('login')
        password = kwargs.get('password')
        if not login or not password:
            return None
        user = cls.query.filter_by(login=login).first()
        if not user or not check_password_hash(user.password, password):
            return None
        return user

    def jsonify(self):
        return dict(id=self.id, login=self.login, password=self.password,
                    email=self.email)
