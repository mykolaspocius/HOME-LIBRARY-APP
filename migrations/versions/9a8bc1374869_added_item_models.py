"""Added item models

Revision ID: 9a8bc1374869
Revises: 7aa5e5656013
Create Date: 2024-11-10 10:54:29.082769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a8bc1374869'
down_revision = '7aa5e5656013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('generos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('padre_id', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Enum('original', 'ausente', 'copia', name='estado_enum'), nullable=False),
    sa.Column('tipo', sa.Enum('archivo', 'libro', 'partitura', 'grabacion', name='tipo_enum'), nullable=False),
    sa.Column('lugar', sa.Enum('biblioteca', 'otro', name='lugar_enum'), nullable=False),
    sa.Column('info_lugar', sa.String(length=70), nullable=False),
    sa.Column('descripcion', sa.String(length=200), nullable=False),
    sa.Column('estanteria', sa.Integer(), nullable=False),
    sa.Column('balda', sa.Integer(), nullable=False),
    sa.Column('carpeta', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('digitalizado', sa.Boolean(), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['padre_id'], ['items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('temas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('libros',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=False),
    sa.Column('edicion', sa.String(length=20), nullable=False),
    sa.Column('genero_id', sa.Integer(), nullable=False),
    sa.Column('tema_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genero_id'], ['generos.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['tema_id'], ['temas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('libro_autor',
    sa.Column('autor', sa.Integer(), nullable=False),
    sa.Column('libro', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['autor'], ['personas.id'], ),
    sa.ForeignKeyConstraint(['libro'], ['libros.id'], ),
    sa.PrimaryKeyConstraint('autor', 'libro')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('libro_autor')
    op.drop_table('libros')
    op.drop_table('temas')
    op.drop_table('personas')
    op.drop_table('items')
    op.drop_table('generos')
    # ### end Alembic commands ###
