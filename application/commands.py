from application.extensions import db
import click
from flask.cli import with_appcontext


from application.models import User, Trainer, Pupil


@click.command('init_db')
@with_appcontext
def initialize():

    db.drop_all()
    db.create_all()
    db.session.commit()


@click.command('populate_db')
@with_appcontext
def populate():

    admin_user = User(email="admin@gmail.com",
                      username="admin",
                      password="password123",
                      role="admin")
    admin_user.save()

    trainer_user = User(email="trainer@gmail.com",
                        username="trainer",
                        password="password123",
                        role="trainer")

    trainer_user.save()
    trainer = Trainer()
    trainer.create(user_id=trainer_user.id, name=trainer_user.username)

    pupil_user = User(email="pupil@gmail.com",
                      username="pupil",
                      password="password123",
                      role="pupil")

    pupil_user.save()
    pupil = Pupil()
    pupil.create(user_id=pupil_user.id, name=pupil_user.username)
