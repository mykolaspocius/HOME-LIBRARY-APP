from app.main import bp
from flask import flash, render_template
from app.forms import UserLoginForm,UserRegisterForm
from app.db_models.user import Usuario
from app.extentions import sql_db

@bp.route('/')
def index():
    return render_template("main/index.html")

@bp.route('/login',methods=['GET','POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(nombre=form.username.data).first()
        if user is None:
            form.username.errors.append(f"Usuario {form.username.data} no existe.")
        else:
            if user.check_password(form.password.data):
                return "Logueado con exito"
            else:
                form.password.errors.append(f"El password para {form.username.data} incorrecto.")
    
    for field, errors in form.errors.items():
        for error in errors:
            flash(f'Error en {getattr(form, field).label.text}: {error}')
    return render_template("main/login.html",form=form)

@bp.route('/register',methods=['GET','POST'])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        existing_user = Usuario.query.filter_by(nombre=form.username.data).first()
        if existing_user is None:
            user = Usuario(nombre=form.username.data,nombre_rol="usuario")
            user.set_password(form.password.data)
            sql_db.session.add(user)
            sql_db.session.commit()
            return "Registrado con exito"
        else:
            form.username.errors.append(f"Usuario con nombre {form.username.data} ya existe.")
    
    for field, errors in form.errors.items():
        for error in errors:
            flash(f'Error en {getattr(form, field).label.text}: {error}')
    return render_template("main/register.html",form=form)

