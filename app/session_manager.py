from app.db_models.item import Genero,Tema,Persona

class SesionManager():
    def initiate_new_book_data(session):
        session['new_book_data']={
            "step":1,
            "titulo":None,
            "edicion":None,
            "genero":{"data":None,"choices":[(p.nombre, p.nombre) for p in Genero.query.all()]},
            "tema":{"data":None,"choices":[(t.nombre, t.nombre) for t in Tema.query.all()]},
            "autores":{"data":None,"choices":[(p.nombre, p.nombre) for p in Persona.query.all()]}
        }

