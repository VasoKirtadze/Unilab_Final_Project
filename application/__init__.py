from flask import Flask
from application.extensions import db, migrate, login_manager, mail
from flask_admin.menu import MenuLink
from application.models import User
from application.admin import admin, UserView
from application.config import Config
from application.commands import initialize, populate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_login(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

    mail.init_app(app)

    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_link(MenuLink(name='Home', url='/'))


def register_blueprints(app):
    from application.public.views import public_blueprint
    app.register_blueprint(public_blueprint)

    from application.users.views import user_blueprint
    app.register_blueprint(user_blueprint, name="users_blueprint", url_prefix='/user')

    from application.trainers.views import trainer_blueprint
    app.register_blueprint(trainer_blueprint, url_prefix='/trainer')

    from application.pupils.views import pupils_blueprint
    app.register_blueprint(pupils_blueprint, url_prefix='/pupil')


def register_login(app):
    login_manager.init_app(app)
    login_manager.login_view = 'users_blueprint.user_login'


def register_commands(app):
    app.cli.add_command(initialize)
    app.cli.add_command(populate)
