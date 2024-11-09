from app.db_models.user import Usuario,Rol,Permiso
from app.extentions import sql_db
import os

def register(app):
    # CLI command to seed data
    @app.cli.command("seed_db")
    def seed():
        # Check if data already exists to avoid duplicate entries
        if not Rol.query.first():
        
            p_ver=Permiso(nombre="ver",valor=1)
            p_crear=Permiso(nombre="crear",valor=2)
            p_borrar=Permiso(nombre="borrar",valor=4)
            p_actualizar=Permiso(nombre="actualizar",valor=8)
            p_gestionar_usuarios=Permiso(nombre="gestion_usuarios",valor=16)
            sql_db.session.add_all([p_ver,p_crear,p_borrar,p_actualizar,p_gestionar_usuarios])
            sql_db.session.commit()

            admin_rol = Rol(nombre="admin")
            user_rol = Rol(nombre="usuario")
            sql_db.session.add(admin_rol)
            sql_db.session.add(user_rol)
            sql_db.session.commit()
            admin_rol.permisos.extend([p_ver,p_crear,p_borrar,p_actualizar,p_gestionar_usuarios])
            user_rol.permisos.extend([p_ver,p_crear,p_borrar,p_actualizar])
            
            u1 = Usuario(nombre="admin",nombre_rol=admin_rol.nombre)
            u1.set_password(os.environ.get('PSW_ADMIN'))

            sql_db.session.add_all([u1])
            sql_db.session.commit()
            print("Database seeded!")
        else:
            print("Database already seeded.")

    @app.cli.command("show_tables")
    def show():
        print("Tables in the database:", sql_db.metadata.tables.keys())