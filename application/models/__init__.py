from application.extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Trainer(db.Model, UserMixin):
    __tablename__ = 'test_trainers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    role = db.Column(db.String(64))
    username = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(225))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    @classmethod
    def find_mail(cls, temp_mail):
        return cls.query.filter_by(email=temp_mail).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


class Pupil(db.Model, UserMixin):
    __tablename__ = 'test_pupils'


    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    role = db.Column(db.String(64))
    username = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(225))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    @classmethod
    def find_mail(cls, temp_mail):
        return cls.query.filter_by(email=temp_mail).first()

    def save(self):
        db.session.add(self)
        db.session.commit()








class User(db.Model, UserMixin):
    __tablename__ = 'test_users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    role = db.Column(db.String(64))
    username = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(225))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    @classmethod
    def find_mail(cls, temp_mail):
        return cls.query.filter_by(email=temp_mail).first()

    def save(self):
        db.session.add(self)
        db.session.commit()






if __name__ == '__main__':
    trainer1 = Trainer(email='radnom@gmail.com',
                       username="random",
                       password="12314")

    print(hasattr(trainer1, 'username'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)




class BaseModel():
    id = db.Column(db.Integer(), primary_key=True)

    def create(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

            self.save()

    @classmethod
    def read_all(cls):
         return cls.query.all()


    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def save(self):
        db.session.add(self)
        db.session.commit()




