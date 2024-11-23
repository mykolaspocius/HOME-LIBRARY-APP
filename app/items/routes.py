from app.items import bp
from flask import flash, render_template, request, session, redirect, url_for
from flask_login import login_required
from app.forms import ItemForm
from app.db_models.item import Libro,Genero,Tema,Persona

button_text={
    1 : "Comenzar",
    2 : "Siguiente",
    3 : "Siguiente",
    4 : "Siguiente",
    5 : "Siguiente",
    6 : "Finalizar y guardar datos"
}

def getButtonText(step):
    return button_text[step]

def session_to_form(form,data):
    for field in data.keys():
        if field != "step" and data[field] != None:
            if field in ["genero","tema"]:
                form[field].data = data[field]["data"]
                form[field].choices = data[field]["choices"]
            else:
                form[field].data = data[field]


@bp.route('/')
@login_required
def index():
    return render_template("items/index.html")

@bp.route('/new',methods=['GET','POST'])
@login_required
def new():
    if not 'new_book_data' in session:
            return "no book data"
    form = ItemForm()
    if form.is_submitted():
        # for now, later erase
        session.pop('new_book_data')
        return "item registred"

    return render_template('items/new.html',form=form)
    
