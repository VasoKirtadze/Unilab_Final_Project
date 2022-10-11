from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, logout_user

public_blueprint = Blueprint('public',
                             __name__,
                             template_folder='../templates')


@public_blueprint.route('/')
@public_blueprint.route('/home')
def home_page() -> str:
    return render_template('home.html')


@public_blueprint.route('/welcome')
@login_required
def welcome():

    return render_template('welcome.html')


@public_blueprint.route('/logout')
def user_logout():
    logout_user()

    return redirect(url_for('public.home_page'))


@public_blueprint.route('/question')
def question():
    return render_template('question.html')
