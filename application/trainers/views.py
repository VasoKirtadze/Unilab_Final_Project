from flask import render_template, redirect, url_for, Blueprint, request, flash, session
from flask_login import login_user, current_user, logout_user
from application.trainers.forms import RegistrationForm, LoginForm
from application.models import User, load_user, Trainer, Pupil, Parameters

trainer_blueprint = Blueprint('trainer',
                              __name__,
                              template_folder='templates/trainers')



@trainer_blueprint.route('/trainers/', methods=['GET', 'POST'])
def show_trainers():
    my_trainers = Trainer.query.all()

    if request.method == 'POST':
        name = request.form['Chosen_coach']
        my_coach = Trainer.query.filter_by(name=name).first()

        _id = my_coach.user_id
        # print(_id)
        return redirect(url_for('pupil.pupil_gauges', _id=_id))

    return render_template('coaches.html', trainers=my_trainers)


@trainer_blueprint.route('/my_pupils', methods=['GET', 'POST'])
def my_pupils():
    trainer = Trainer.query.filter_by(user_id=current_user.id).first()
    my_pupils = trainer.pupils

    if request.method == 'POST':
        pupil_name = request.form['Chosen_pupil']

        return redirect(url_for('trainer.program', pupil_name=pupil_name))


    return render_template('my_pupils.html', pupils=my_pupils)

@trainer_blueprint.route('/program/<pupil_name>', methods=['GET', 'POST'])
def program(pupil_name):
    pupil = Pupil.query.filter_by(name=pupil_name).first()

    parameter = Parameters.query.get(pupil.parameter_id)


    return render_template('program.html', parameter=parameter, pupil=pupil)