from application.models import User
from application.extensions import db


class Trainer(db.Model, User):
    __tablename__ = "Trainers"
    pass


class Pupil(db.Model, User):
    pass


if __name__ == '__main__':
    trainer1 = Trainer

    print(hasattr(trainer1, 'username'))
