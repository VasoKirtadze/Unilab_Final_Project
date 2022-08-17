from application.extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    role = db.Column(db.String(64))
    username = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(225))

    def __init__(self, email, username, role, password):
        self.email = email
        self.username = username
        self.role = role
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    @classmethod
    def find_mail(cls, temp_mail):
        return cls.query.filter_by(email=temp_mail).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


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


class Trainer(db.Model, BaseModel):
    user_id = db.Column(db.Integer())
    name = db.Column(db.String(64))

    pupils = db.relationship('Pupil', backref='trainer')


class Pupil(db.Model, BaseModel):
    user_id = db.Column(db.Integer())
    name = db.Column(db.String(64))
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))

    parameter_id = db.Column(db.Integer, db.ForeignKey('parameters.id'))



class Parameters(db.Model, BaseModel):


    age = db.Column(db.Integer())
    height = db.Column(db.Integer())
    weight = db.Column(db.Integer())
    health = db.Column(db.String(256))
    purpose = db.Column(db.String(64))










