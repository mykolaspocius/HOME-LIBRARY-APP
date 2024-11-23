from app.books import bp
from flask import flash, render_template, request, session, redirect, url_for
from flask_login import login_required
from app.forms import LibroForm
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
    return render_template("books/index.html")

@bp.route('/new',methods=['GET','POST'])
@login_required
def new():
    if request.method == 'GET':
        if 'new_book_data' in session:
            session.pop('new_book_data')
        session['new_book_data']={
            "step":1,
            "titulo":None,
            "edicion":None,
            "genero":{"data":None,"choices":[(p.nombre, p.nombre) for p in Genero.query.all()]},
            "tema":{"data":None,"choices":[(t.nombre, t.nombre) for t in Tema.query.all()]},
            "autores":{"data":None,"choices":[(p.nombre, p.nombre) for p in Persona.query.all()]}
        }
        session.modified = True

    form = LibroForm()
    if form.is_submitted():
        step=session['new_book_data'].get("step")
        if "back" in request.form and request.form["back"] == "true":
            session['new_book_data']["step"]=max(step - 1, 1)
            
        elif step==1:
            session['new_book_data']["step"]=step+1
        elif step==2:
            form.validate()
            session['new_book_data']["titulo"]=form.titulo.data
            session['new_book_data']["edicion"]=form.edicion.data
            session['new_book_data']["step"]=step+1
        elif step==3:
            if form.genero.data:
                session['new_book_data']["genero"]["data"]=form.genero.data
                if form.genero.data not in [choice[0] for choice in session['new_book_data']["genero"]["choices"]]: 
                    session['new_book_data']["genero"]["choices"].append((form.genero.data, form.genero.data))
            session['new_book_data']["step"]=step+1
        elif step==4:
            if form.tema.data:
                session['new_book_data']["tema"]["data"]=form.tema.data
                if form.tema.data not in [choice[0] for choice in session['new_book_data']['tema']['choices']]:
                    session['new_book_data']["tema"]["choices"].append((form.tema.data, form.tema.data))


            session['new_book_data']["step"]=step+1
        elif step==5:
            session['new_book_data']["autores"]=form.autores.data
            session['new_book_data']["step"]=step+1
        elif step==6:
            return redirect(url_for("items.new"))
        
        session.modified = True
        print(session['new_book_data'])
        session_to_form(form,session['new_book_data'])
    
    return render_template(
        "books/new.html",
        step=session['new_book_data'].get("step"),
        form=form,
        button_text_value=getButtonText(session['new_book_data'].get("step"))
    )
