from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    """
    class which allows people to register
    validators check the correctness
    """

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        """
        validation if username is already taken in the db to avoid 2nd registration
        :return:('Validation Message')
        """
        user = User.query.filter_by(username=username.data).first()
        if user==True:
           raise ValidationError('Username already taken. Please choose another one.')

    def validate_email(self,email):
        """
        validation if email is already taken in the db to avoid 2nd registration
        :return:('Validation Message')
        """
        user = User.query.filter_by(email=email.data).first()
        if user==True:
            raise ValidationError('Email already taken. Please choose another one.')

class LoginForm(FlaskForm):
    """
    Login for users.
    Remember allows user to stay logged after closing browsers.
    Secret key will protect against modifying cookies, attacks etc.
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    """
    class which allows people to update their info
    validators check the correctness
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        """
        checks if username is different than current one and whether the username is already taken
        :raise:('Validation Message')
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user==True:
               raise ValidationError('Username already taken. Please choose another one.')

    def validate_email(self,email):
        """
        checks if email is different than current one and whether the email is already taken
        :raise:('Validation Message')
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user==True:
                raise ValidationError('Email already taken. Please choose another one.')
