from urllib.parse import urlsplit
from app.main import bp
from flask import flash, render_template, redirect, request,url_for
from app.forms import UserLoginForm,UserRegisterForm
from app.db_models.user import Usuario
from app.extentions import sql_db
from flask_login import current_user,login_user,logout_user

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
                login_user(user,remember=form.remember_me.data)
                next_page = request.args.get('next')
                if not next_page or urlsplit(next_page).netloc != '':
                    next_page = url_for('main.index')
                return redirect(next_page)
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
            flash(f"Usuario {user.nombre} registrado")
            return redirect(url_for('main.login'))
        else:
            form.username.errors.append(f"Usuario con nombre {form.username.data} ya existe.")
    
    for field, errors in form.errors.items():
        for error in errors:
            flash(f'Error en {getattr(form, field).label.text}: {error}')
    return render_template("main/register.html",form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

