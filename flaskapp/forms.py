from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# This class will define the form that we will create.
class RegistrationForm(FlaskForm):
    # Data required means it cant be empty , length is the max amount of charachters.
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # Stringfield = the form only accepts string.
    email = StringField('Email', validators=[DataRequired(), Email(),])
    # Passwordfield = the form only accespts passwords.
    password = PasswordField('Password', validators=[DataRequired()])
    # Confirm password checks on the password field above ^ and make sure it is EqualTo
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    # Stringfield = the form only accepts string.
    email = StringField('Email', validators=[DataRequired(), Email(),])
    # Passwordfield = the form only accespts passwords.
    password = PasswordField('Password', validators=[DataRequired()])
    # Remembers the users login. Imported from wtforms
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
