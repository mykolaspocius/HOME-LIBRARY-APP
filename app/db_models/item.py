from app.extentions import sql_db
from sqlalchemy import Boolean, Enum, String,Integer,ForeignKey,Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Item(sql_db.Model):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    padre_id : Mapped[int] = mapped_column(Integer, ForeignKey("items.id"))
    estado: Mapped[str] = mapped_column(Enum('original', 'ausente', 'copia', name='estado_enum'))
    tipo: Mapped[str] = mapped_column(Enum('archivo', 'libro', 'partitura', 'grabacion', name='tipo_enum'))
    lugar: Mapped[str] = mapped_column(Enum('biblioteca', 'otro', name='lugar_enum'))
    info_lugar: Mapped[str] = mapped_column(String(70))
    descripcion: Mapped[str] = mapped_column(String(200))
    estanteria: Mapped[int] = mapped_column(Integer)
    balda: Mapped[int] = mapped_column(Integer)
    carpeta: Mapped[int] = mapped_column(Integer)
    numero: Mapped[int] = mapped_column(Integer)
    digitalizado: Mapped[bool] = mapped_column(Boolean, nullable=False)
    url: Mapped[str] = mapped_column(String(100))
    componentes : Mapped[list["Item"]] = relationship()
    libros : Mapped[list["Libro"]] = relationship(back_populates="item")

class Genero(sql_db.Model):
    __tablename__ = 'generos'
    id : Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(20))
    libros : Mapped[list["Libro"]] = relationship(back_populates="genero")

class Tema(sql_db.Model):
    __tablename__ = 'temas'
    id : Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(20))
    libros : Mapped[list["Libro"]] = relationship(back_populates="tema")

class LibroAutor(sql_db.Model):
    __tablename__ = 'libro_autor'
    autor : Mapped[int] = Column(Integer,ForeignKey('personas.id'), primary_key=True)
    libro : Mapped[int] = Column(Integer,ForeignKey('libros.id'), primary_key=True)

class Persona(sql_db.Model):
    __tablename__ = 'personas'
    id : Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50))
    libros: Mapped[list["Libro"]] = relationship(secondary=LibroAutor.__table__,back_populates="autores")

class Libro(sql_db.Model):
    __tablename__ = 'libros'
    id : Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(50))
    edicion: Mapped[str] = mapped_column(String(20))
    genero_id : Mapped[int]= mapped_column(Integer,ForeignKey("generos.id"))
    tema_id : Mapped[int]= mapped_column(Integer,ForeignKey("temas.id"))
    item_id : Mapped[int] = mapped_column(Integer,ForeignKey("items.id"))
    autores: Mapped[list["Persona"]] = relationship(secondary=LibroAutor.__table__, back_populates="libros")
    genero: Mapped["Genero"] = relationship("Genero", back_populates="libros")
    tema: Mapped["Tema"] = relationship("Tema", back_populates="libros")
    item: Mapped["Item"] = relationship("Item", back_populates="libros")