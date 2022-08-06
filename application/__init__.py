from flask import Flask, redirect, url_for
from application.extensions import db, migrate, login_manager, admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from application.models import User


class UserView(ModelView):

    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('public.home_page'))


    can_create = False

    column_searchable_list = ['username']

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

    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_link(MenuLink(name='Home', url='/'))

def register_blueprints(app):
    from application.public.views import public_blueprint
    app.register_blueprint(public_blueprint)

    from application.user.views import user_blueprint
    app.register_blueprint(user_blueprint, name="users_blueprint", url_prefix='/user')


def register_login(app):
    login_manager.init_app(app)
    login_manager.login_view = 'users_blueprint.user_login'