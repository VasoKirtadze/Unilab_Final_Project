from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField, EmailField, RadioField, IntegerField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField

from application.models import User


class RegistrationForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    role = RadioField(validators=[DataRequired()], choices=[('trainer', 'Trainer'), ('pupil', 'Pupil')])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField('confirm password', validators=[DataRequired()])
    agree = BooleanField(validators=[DataRequired()])
    file = FileField('Upload File')
    submit = SubmitField('Register')

    def validate_by_mail(self):
        temp_mail = self.email.data
        if User.find_mail(temp_mail):
            raise ValidationError("This email is already used")


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UpdateForm(FlaskForm):
    email = EmailField('email')
    username = StringField('username')
    age = IntegerField("Age")
    height = IntegerField("Height")
    weight = IntegerField("Weight")
    health = StringField("Health")
    purpose = StringField("Purpose")
