from app.main import bp
from flask import flash, render_template
from app.forms import UserLoginForm,UserRegisterForm
from app.db_models.user import Usuario

@bp.route('/')
def index():
    return render_template("main/index.html")

@bp.route('/login',methods=['GET','POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        return "Logueado con exito"
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error en {getattr(form, field).label.text}: {error}')
        return render_template("main/login.html",form=form)

@bp.route('/register',methods=['GET','POST'])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        return "Registrado con exito"
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error en {getattr(form, field).label.text}: {error}')
        return render_template("main/register.html",form=form)

