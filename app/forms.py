from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class CustomDataRequired(DataRequired):
    def __init__(self, message=None):
        if message is None:
            message="Este campo es obligatorio"
        super().__init__(message=message)

class UserLoginForm(FlaskForm):
    username = StringField('Usuario', validators=[CustomDataRequired()])
    password = PasswordField('Password', validators=[CustomDataRequired()])
    remember_me = BooleanField('Recordar')
    submit = SubmitField('Entrar')

class UserRegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[CustomDataRequired()])
    password = PasswordField('Password', validators=[CustomDataRequired()])
    password_repeat = PasswordField('Repetir password', validators=[CustomDataRequired(),EqualTo("password",message="Los passwords no son iguales")])
    submit = SubmitField('Registrarme')