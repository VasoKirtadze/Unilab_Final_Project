from flask import Flask
from application.extensions import db, migrate, login_manager



def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    register_extensions(app)
    register_blueprints(app)
    register_login(app)
    return app



def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from application.public.views import public_blueprint
    app.register_blueprint(public_blueprint)


def register_login(app):
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'