from flask import render_template, redirect, Blueprint, url_for, request
from flask_login import login_user
from application.extensions import db
from application.models import User
from application.user.forms import RegistrationForm, LoginForm


user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates')


@user_blueprint.route('/register')
def user_register():
    my_form = RegistrationForm()


    return render_template('register.html', form=my_form)






@user_blueprint.route('/login')
def user_login():
    my_form = LoginForm()


    return render_template('login.html', form=my_form)
