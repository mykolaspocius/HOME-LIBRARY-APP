from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, StringField, PasswordField, BooleanField, SubmitField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

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

class LibroForm(FlaskForm):
    titulo = StringField('Titulo', validators=[CustomDataRequired(),Length(min=1,max=50)])
    edicion = StringField('Edicion', validators=[Length(min=0,max=20)])
    genero = SelectField("Genero",validators=[CustomDataRequired()])
    tema = SelectField("Tema",validators=[CustomDataRequired()])
    autores = SelectMultipleField("Autores",validators=[CustomDataRequired()])
    submit = SubmitField('Registrar')