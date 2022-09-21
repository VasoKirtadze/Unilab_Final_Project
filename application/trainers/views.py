from flask import render_template, redirect, url_for, Blueprint, request, flash, session
from flask_login import login_user, current_user, logout_user
from application.trainers.forms import RegistrationForm, LoginForm, ProgramForm
from application.models import User, load_user, Trainer, Pupil, Parameters, Workouts, Diet
from application.mails.mymail import send_mail
trainer_blueprint = Blueprint('trainer',
                              __name__,
                              template_folder='templates/trainers')



@trainer_blueprint.route('/trainers/', methods=['GET', 'POST'])
def show_trainers():
    my_trainers = Trainer.query.all()
    pupil = Pupil.query.filter_by(user_id = current_user.id).first()

    if pupil.trainer_id is not None:
        return redirect(url_for('public.question'))
    if request.method == 'POST':
        name = request.form['Chosen_coach']
        my_coach = Trainer.query.filter_by(name=name).first()

        _id = my_coach.user_id

        return redirect(url_for('pupil.pupil_gauges', _id=_id))

    return render_template('coaches.html', trainers=my_trainers)


@trainer_blueprint.route('/my_pupils', methods=['GET', 'POST'])
def my_pupils():
    trainer = Trainer.query.filter_by(user_id=current_user.id).first()
    my_pupils_demo = trainer.pupils
    my_pupils = my_pupils_demo[::-1]
    if request.method == 'POST':
        pupil_name = request.form['Chosen_pupil']

        return redirect(url_for('trainer.program', pupil_name=pupil_name))


    return render_template('my_pupils.html', pupils=my_pupils)

@trainer_blueprint.route('/program/<pupil_name>', methods=['GET', 'POST'])
def program(pupil_name):
    my_form = ProgramForm()
    pupil = Pupil.query.filter_by(name=pupil_name).first()
    parameter = Parameters.query.get(pupil.parameter_id)
    user = User.query.get(pupil.user_id)
    if my_form.validate_on_submit():
        day1 = my_form.day1.data
        day2 = my_form.day2.data
        day3 = my_form.day3.data
        day4 = my_form.day4.data
        day5 = my_form.day5.data
        day6 = my_form.day6.data
        day7 = my_form.day7.data
        diet = my_form.diet.data
        my_diet = Diet()
        my_diet.create(food=diet)
        workout = Workouts()
        workout.create(day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, day6=day6, day7=day7)
        pupil.update(workout_id=workout.id, diet_id=my_diet.id)
        send_mail(user.email, """Your program is finished!""")
        flash("Program added")
        return redirect(url_for('trainer.my_pupils'))

    return render_template('program.html', parameter=parameter, pupil=pupil, form=my_form)