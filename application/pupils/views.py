from flask import render_template, redirect, url_for, Blueprint, request, flash
from flask_login import login_user, current_user, logout_user

from application.pupils.forms import RegistrationForm, AboutForm
from application.models import User, load_user, Trainer, Pupil, Parameters, Workouts, Diet

pupils_blueprint = Blueprint('pupil',
                              __name__,
                              template_folder='templates/pupils')



@pupils_blueprint.route('/gauges/<_id>', methods=["GET", "POST"])
def pupil_gauges(_id):

    my_form = AboutForm()
    trainer = Trainer.query.filter_by(user_id=_id).first()

    if my_form.validate_on_submit():
        pupil = Pupil.query.filter_by(name=current_user.username).first()

        pupil.update(trainer_id=trainer.id)
        parameter = Parameters()
        parameter.create(age=my_form.age.data,
                                      height=my_form.height.data,
                                      weight=my_form.weight.data,
                                      health=my_form.health.data,
                                      purpose=my_form.purpose.data,
                                    days=my_form.days.data)
        pupil.update(parameter_id=parameter.id)

        return redirect(url_for('pupil.pupil_result'))

    return render_template("pupil_info.html", form=my_form)

@pupils_blueprint.route('/my_program')
def my_program():
    pupil = Pupil.query.filter_by(user_id=current_user.id).first()
    my_workout = Workouts.query.get(pupil.workout_id)
    my_diet = Diet.query.get(pupil.diet_id)
    return render_template('my_program.html', workout=my_workout, diet=my_diet, pupil=pupil)

@pupils_blueprint.route('/result')
def pupil_result():

    return render_template('result.html')















