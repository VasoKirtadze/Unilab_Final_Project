from flask import render_template, redirect, url_for, Blueprint, request, flash, session
from flask_login import login_user, current_user, logout_user
from application.trainers.forms import RegistrationForm, LoginForm
from application.models import User, load_user, Trainer

trainer_blueprint = Blueprint('trainer',
                              __name__,
                              template_folder='templates/trainers')


@trainer_blueprint.route('/register', methods=['GET', 'POST'])
def register_trainer():
    my_form = RegistrationForm()

    if my_form.validate_on_submit():

        trainer = Trainer(email=my_form.email.data,
                    username=my_form.username.data,
                    password=my_form.password.data,
                    )
        trainer.role = 'trainer'
        trainer.save()
        flash("registration went successfully")
        return redirect(url_for('users_blueprint.user_login'))

    return render_template('register_trainer.html', form=my_form)


@trainer_blueprint.route('/trainers/', methods=['GET', 'POST'])
def show_trainers():
    my_trainers = Trainer.query.all()

    if request.method == 'POST':
        name = request.form['Chosen_coach']
        my_coach = Trainer.query.filter_by(username=name).first()
        # print(my_coach.username)
        # session['trainer'] = my_coach
        _id = my_coach.id
        # print(_id)
        return redirect(url_for('pupil.pupil_gauges', trainer_id=_id))

    return render_template('coaches.html', trainers=my_trainers)

