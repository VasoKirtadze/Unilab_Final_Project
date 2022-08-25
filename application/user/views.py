from flask import render_template, redirect, Blueprint, url_for, request, flash
from flask_login import login_user, current_user, logout_user
from application.extensions import db
from application.models import User, load_user, Trainer, Pupil, Parameters
from application.user.forms import RegistrationForm, LoginForm, UpdateForm
from flask_login import login_required



user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates')

@user_blueprint.route('/')
@login_required
def user_profile():
    pupil = Pupil.query.filter_by(user_id=current_user.id).first()
    parameter = Parameters.query.get(pupil.parameter_id)
    my_form = UpdateForm()
    trainer = Trainer.query.get(pupil.trainer_id)

    if my_form.validate_on_submit():
        pass


    return render_template('profile.html', pupil=pupil, parameter=parameter)



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
        if my_form.role.data == 'trainer':
            trainer = Trainer()
            trainer.create(user_id=user.id, name=my_form.username.data)
        else:
            pupil = Pupil()
            pupil.create(user_id=user.id, name=my_form.username.data)
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
            flash(f"Logged in successfully, Welcome {current_user.email}")

            next = request.args.get('next')

            if next is None:
                next = url_for('public.home_page')

            return redirect(next)

        else:
            flash("User doesnt exist")


    return render_template('login.html', form=my_form)



@user_blueprint.route('/logout')
def user_logout():
    logout_user()

    return redirect(url_for('public.home_page'))











