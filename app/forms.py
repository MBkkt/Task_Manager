from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField, SelectField,
    SelectMultipleField, TextAreaField
)
from wtforms.validators import ValidationError, DataRequired
from app.models import User, Task


class RegistrationForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    type = SelectField('Account type', coerce=int,
                       choices=[(0, 'Worker'), (1, 'Admin')])
    submit = SubmitField('Sign in')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user is not None:
            raise ValidationError('Enter another login')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Enter another email')


class ProfileForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    type = SelectField(
        'Account type', coerce=int, choices=[(0, 'Worker'), (1, 'Admin')]
    )
    delete = BooleanField('Delete')
    submit = SubmitField('Save')


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')


class EditTaskForPerformer(FlaskForm):
    status = SelectField(
        'Status', coerce=int,
        choices=[(0, 'TO DO'), (1, 'IN PROGRESS'), (2, 'ON REVIEW')]
    )
    submit = SubmitField('Save')


class EditTaskForOwner(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    status = SelectField(
        'Status', coerce=int, choices=[
            (0, 'TO DO'), (1, 'IN PROGRESS'), (2, 'ON REVIEW'),
            (3, 'DONE'),
        ]
    )
    users_id = SelectMultipleField(
        'Performers', coerce=int, validators=[DataRequired()]
    )
    delete = BooleanField('Delete')
    submit = SubmitField('Save')


class AddTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

    users_id = SelectMultipleField(
        'Performers', coerce=int, validators=[DataRequired()]
    )
    submit = SubmitField('Add')

    def validate_title(self, title):
        task = Task.query.filter_by(title=title.data).first()
        if task is not None:
            raise ValidationError('Enter another title')
