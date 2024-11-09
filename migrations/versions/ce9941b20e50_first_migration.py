"""first migration

Revision ID: ce9941b20e50
Revises: 
Create Date: 2024-11-09 18:02:49.571091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce9941b20e50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permisos',
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('nombre')
    )
    op.create_table('roles',
    sa.Column('nombre', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('nombre')
    )
    op.create_table('rol_permiso',
    sa.Column('rol_id', sa.String(length=10), nullable=False),
    sa.Column('permiso_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['permiso_id'], ['permisos.nombre'], ),
    sa.ForeignKeyConstraint(['rol_id'], ['roles.nombre'], ),
    sa.PrimaryKeyConstraint('rol_id', 'permiso_id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('nombre_rol', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['nombre_rol'], ['roles.nombre'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    op.drop_table('rol_permiso')
    op.drop_table('roles')
    op.drop_table('permisos')
    # ### end Alembic commands ###