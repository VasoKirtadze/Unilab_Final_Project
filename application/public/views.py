from flask import render_template, redirect, url_for, Blueprint

public_blueprint = Blueprint('public',
                             __name__,
                             template_folder='../templates')

@public_blueprint.route('/')
@public_blueprint.route('/home')
def home_page():
    return render_template('home.html')





