from flask_wtf import FlaskForm
from wtforms import IntegerField,SelectField, SelectMultipleField, StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Optional, URL

class CustomDataRequired(DataRequired):
    def __init__(self, message=None, invalid_values=None):
        if message is None:
            message="Este campo es obligatorio"
        self.invalid_values = invalid_values or [None, '', 'None']
        super().__init__(message=message)
        
    def __call__(self, form, field):
        # Check for invalid values
        if field.data in self.invalid_values:
            raise ValidationError(self.message)
        super().__call__(form, field)

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
    submit = SubmitField('Siguiente')

class ItemForm(FlaskForm):
    padre_id = IntegerField('Id item padre',validators=[Optional()])
    estado = SelectField('Estado',choices=['','original', 'ausente', 'copia'], validators=[CustomDataRequired()])
    tipo = SelectField('Tipo',choices=['','archivo', 'libro', 'partitura', 'grabacion'], validators=[CustomDataRequired()])
    lugar = SelectField("Lugar",choices=['','biblioteca', 'otro'], validators=[CustomDataRequired()])
    info_lugar = StringField('Descripcion_lugar',validators=[Length(min=1,max=70),Optional()])
    descripcion = StringField('Descripcion',validators=[Length(max=200),Optional()])
    estanteria = IntegerField("Estanteria", validators=[Optional()])
    balda = IntegerField("Balda",validators=[Optional()])
    carpeta = IntegerField("Carpeta",validators=[Optional()])
    numero = IntegerField("Numero",validators=[Optional()])
    digitalizado = BooleanField("Digitalizado")
    url = StringField("URL",validators=[Length(min=1,max=100),URL(),Optional()])
    submit = SubmitField('Siguiente')

class RegisterForm(FlaskForm):
    submit = SubmitField('Registrar elemento')

     