from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import validators

class UserForm(Form):
    id=IntegerField('id')
    name = StringField('nombre')
    surname = StringField('apellidos')
    email = EmailField('correo')

