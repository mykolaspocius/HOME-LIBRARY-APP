from flask_wtf import FlaskForm
from wtforms import IntegerField,SelectField, SelectMultipleField, StringField, PasswordField, BooleanField, SubmitField
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
    edicion = StringField('Edicion',  validators=[Length(min=0,max=20)])
    genero = SelectField("Genero",choices=[],validators=[CustomDataRequired()])
    tema = SelectField("Tema",choices=[],validators=[CustomDataRequired()])
    autores = SelectMultipleField("Autores",choices=[],validators=[CustomDataRequired()])
    submit = SubmitField('Registrar')

class ItemForm(FlaskForm):
    padre_id = IntegerField('Id item primario')
    estado = SelectField('Estado',choices=['original', 'ausente', 'copia'])
    tipo = SelectField('Tipo',choices=['archivo', 'libro', 'partitura', 'grabacion'])
    lugar = SelectField("Lugar",choices=['biblioteca', 'otro'])
    info_lugar = StringField('Descripcion_lugar',validators=[Length(max=70)])
    descripcion = StringField('Descripcion',validators=[Length(max=200)])
    estanteria = IntegerField("Estanteria")
    balda = IntegerField("Balda")
    carpeta = IntegerField("Carpeta")
    numero = IntegerField("Numero")
    digitalizado = BooleanField("Digitalizado")
    url = StringField("URL",validators=[Length(max=100)])
    submit = SubmitField('Registrar')

     