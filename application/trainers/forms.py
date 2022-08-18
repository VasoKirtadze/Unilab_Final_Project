from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField, EmailField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from application.models import User

class RegistrationForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])

    password = PasswordField('password', validators=[DataRequired(), EqualTo('pass_confirm')])
    pass_confirm = PasswordField('confirm password', validators=[DataRequired()])
    bio = TextAreaField()
    agree = BooleanField(validators=[DataRequired()])


    submit = SubmitField('Register')

    def validate_by_mail(self):
        temp_mail = self.email.data
        if User.find_mail(temp_mail):
            raise ValidationError("This email is already used")




class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ProgramForm(FlaskForm):
    day1 = TextAreaField("day1")
    day2 = TextAreaField("day2")
    day3 = TextAreaField("day3")
    day4 = TextAreaField("day4")
    day5 = TextAreaField("day5")
    day6 = TextAreaField("day6")
    day7 = TextAreaField("day7")
    diet = TextAreaField("diet")

    submit = SubmitField('Submit')