from app.extentions import sql_db
from sqlalchemy import String,Integer,ForeignKey,Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class RolPermiso(sql_db.Model):
    __tablename__ = 'rol_permiso'
    rol_id : Mapped[str] = Column(String(10),ForeignKey('roles.nombre'), primary_key=True)
    permiso_id : Mapped[str] = Column(String(20), ForeignKey('permisos.nombre'), primary_key=True)

class Permiso(sql_db.Model):
    __tablename__ = 'permisos'
    nombre : Mapped[str] = mapped_column(String(20), primary_key=True)
    valor : Mapped[int] = mapped_column(Integer, nullable=False)
    roles: Mapped[list["Rol"]] = relationship(secondary=RolPermiso.__table__, back_populates="permisos")

class Rol(sql_db.Model):
    __tablename__ = 'roles'
    nombre : Mapped[str] = Column(String(10), primary_key=True)
    usuarios: Mapped[list["Usuario"]] = relationship(back_populates="rol")
    permisos: Mapped[list["Permiso"]] = relationship(secondary=RolPermiso.__table__, back_populates="roles")

class Usuario(UserMixin,sql_db.Model):
    __tablename__ = 'usuarios'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre : Mapped[str] = mapped_column(String(20),nullable=False)
    password : Mapped[str] = mapped_column(String(255),nullable=False)
    nombre_rol: Mapped[str] = mapped_column(String(10), ForeignKey("roles.nombre"))
    rol : Mapped["Rol"]= relationship(back_populates="usuarios")
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)