from app.items import bp
from flask import flash, render_template, request, session, redirect, url_for
from flask_login import login_required
from app.forms import ItemForm,LibroForm,RegisterForm
from wtforms import validators
from app.db_models.item import Libro,Genero,Tema,Persona
from app.session_manager import SessionManager

class ItemInfo:
    type = None

class ItemPlaceInfo:
    ready = False

def get_item_info_in_session(session):
    item_info = ItemInfo()
    if SessionManager.exists_data_for(session,LibroForm):
        item_info.type = 'libro'
        setattr(item_info,"edit_route","books.new")
        setattr(item_info,"data",SessionManager.get_form_data(session,LibroForm))
    return item_info

def get_item_place_info_in_session(session):
    item_place_info = ItemPlaceInfo()
    if SessionManager.exists_data_for(session,ItemForm):
        item_place_info.ready = True
        setattr(item_place_info,"edit_route","items.new")
        setattr(item_place_info,"data",SessionManager.get_form_data(session,ItemForm))
    return item_place_info

@bp.route('/')
@login_required
def index():
    return render_template("items/index.html")

@bp.route('/new',methods=['GET','POST'])
# @login_required
def new():
    item_info = get_item_info_in_session(session)
    form = ItemForm(data={"tipo":item_info.type})
    form.tipo.render_kw = {'disabled': True}
    
    
    if not item_info.type:
        flash(f'No hay datos sobre el tipo de item que se pretende registrar')

    elif request.method == 'GET':
        if not SessionManager.exists_data_for(session,form):
            SessionManager.create_form_data(session=session,form=form)
        SessionManager.load_form_data(session=session,form=form,exclude=['csrf_token','submit','tipo'])

    else:
        if form.is_submitted():
            if request.form.get("back"):
                return redirect(url_for(item_info.edit_route))
            SessionManager.store_form_data(session,form)
            SessionManager.load_form_data(session=session,form=form,exclude=['csrf_token','submit','tipo'])
            if form.lugar.data == 'biblioteca':
                form.estanteria.validators = [v for v in form.estanteria.validators if not isinstance(v, validators.Optional)]
                form.balda.validators = [v for v in form.balda.validators if not isinstance(v, validators.Optional)]
                form.numero.validators = [v for v in form.numero.validators if not isinstance(v, validators.Optional)]
            if form.lugar.data == 'otro':
                form.info_lugar.validators = [v for v in form.info_lugar.validators if not isinstance(v, validators.Optional)]
            if form.digitalizado.data:
                form.url.validators = [v for v in form.url.validators if not isinstance(v, validators.Optional)]


            if form.validate():
                
                return redirect(url_for("items.register"))
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f'Error en {getattr(form, field).label.text}: {error}')

    return render_template('items/new.html',form=form,item_info=item_info)

@bp.route('/register',methods=['GET','POST'])
# @login_required
def register():
    item_info = get_item_info_in_session(session)
    item_place_info = get_item_place_info_in_session(session)
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('items/register.html',form=form,item_info=item_info,item_place_info=item_place_info)
    elif form.is_submitted():
        if request.form.get("back_to_info"):
            return redirect(url_for(item_info.edit_route))
        if request.form.get("back_to_place"):
            return redirect(url_for(item_place_info.edit_route))
        else:
            return "Gardando datos..."
