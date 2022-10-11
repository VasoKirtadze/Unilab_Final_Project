from flask import render_template, redirect, Blueprint, url_for, request, flash
from flask_login import login_user, current_user, logout_user
from application.models import User, Trainer, Pupil, Parameters
from application.users.forms import RegistrationForm, LoginForm
from flask_login import login_required


user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates')


@user_blueprint.route('/', methods=['POST', 'GET'])
@login_required
def user_profile():
    parameter = None
    pupil = Pupil.query.filter_by(user_id=current_user.id).first()
    trainer = Trainer.query.filter_by(user_id=current_user.id).first()
    user = User.query.get(current_user.id)

    if pupil is not None:
        parameter = Parameters.query.get(pupil.parameter_id)

    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')
        health = request.form.get('health')
        purpose = request.form.get('purpose')
        bio = request.form.get('bio')
        if trainer is not None:
            if email:
                user.email = email
                user.save()
            if username:

                user.username = username
                user.save()
                trainer.update(name=username)
            if bio:
                trainer.update(bio=bio)

        if Pupil is not None:
            if email:
                user.email = email
                user.save()
            if username:
                user.username = username
                user.save()
                pupil.update(name=username)

            if age:
                parameter.update(age=age)
            if height:
                parameter.update(height=height)
            if weight:
                parameter.update(weight=weight)
            if health:
                parameter.update(health=health)
            if purpose:
                parameter.update(purpose=purpose)

    return render_template('profile.html', pupil=pupil, parameter=parameter, trainer=trainer)


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
        if my_form.file.data is not None:
            my_form.file.data.save(f'application/static/uploads/{my_form.username.data}.png')
        if my_form.role.data == 'trainer':
            trainer = Trainer()
            trainer.create(user_id=user.id, name=my_form.username.data)
            if my_form.file.data is not None:
                trainer.update(has_pic=1)

        else:
            pupil = Pupil()
            pupil.create(user_id=user.id, name=my_form.username.data)
            if my_form.file.data is not None:
                pupil.update(has_pic=1)

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
            # flash(f"Logged in successfully, Welcome {current_user.username}")

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
