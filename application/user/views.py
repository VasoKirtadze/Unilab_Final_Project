from flask import render_template, redirect, Blueprint, url_for, request, flash
from flask_login import login_user, current_user, logout_user
from application.extensions import db
from application.models import User, load_user
from application.user.forms import RegistrationForm, LoginForm


user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates')

@user_blueprint.route('/')
def user_profile():
    return render_template('profile.html')



@user_blueprint.route('/register', methods=['GET', 'POST'])
def user_register():
    my_form = RegistrationForm()


    if my_form.validate_on_submit():

        user = User(email=my_form.email.data,
                    username=my_form.username.data,
                    password=my_form.password.data,
                    role=my_form.role.data
                    )
        user.save()
        flash("registration went successfully")
        return redirect(url_for('users_blueprint.user_login'))

    return render_template('register.html', form=my_form)






@user_blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    my_form = LoginForm()

    if my_form.validate_on_submit():
        user = User.find_mail(my_form.email.data)
        if user is not None and user.check_password(my_form.password.data):
            login_user(user)
            flash(f"Logged in successfully, Welcome {current_user.username}")

            next = request.args.get('next')

            if next is None:
                next = url_for('public.home_page')

            return redirect(next)
        elif user is not None and user.check_password(my_form.password.data) is False:
            flash("Password Incorrect")

        else:
            flash("User doesnt exist")



    return render_template('login.html', form=my_form)


@user_blueprint.route('/logout')
def user_logout():
    logout_user()

    return redirect(url_for('public.home_page'))











