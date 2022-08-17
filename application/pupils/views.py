from flask import render_template, redirect, url_for, Blueprint, request, flash
from flask_login import login_user, current_user, logout_user
from application.trainers.forms import LoginForm
from application.pupils.forms import RegistrationForm, AboutForm
from application.models import User, load_user, Trainer, Pupil

pupils_blueprint = Blueprint('pupil',
                              __name__,
                              template_folder='templates/pupils')


@pupils_blueprint.route('/register', methods=['GET', 'POST'])
def register_pupil():
    my_form = RegistrationForm()

    if my_form.validate_on_submit():

        pupil = Pupil(email=my_form.email.data,
                    username=my_form.username.data,
                    password=my_form.password.data,
                    )

        pupil.role = 'pupil'
        pupil.save()
        flash("registration went successfully")
        return redirect(url_for('users_blueprint.user_login'))

    return render_template('register_pupils.html', form=my_form)

@pupils_blueprint.route('/gauges/<trainer_id>', methods=["GET", "POST"])
def pupil_gauges(trainer_id):

    my_form = AboutForm()
    trainer = Trainer.query.get(trainer_id)
    print(current_user.role)
    print(current_user.email)
    if current_user.role == 'pupil':

        current_user.trainer_id = trainer.id
        print(current_user.coach.username)
    if my_form.validate_on_submit():
        print(my_form.age.data)





    return render_template("pupil_info.html", form=my_form)

















