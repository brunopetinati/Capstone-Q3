"""Adicionado usuarios"



Revision ID: 48939ecf5a5d
Revises: 
Create Date: 2021-04-15 13:40:23.768424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48939ecf5a5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=100), nullable=False),
    sa.Column('tecnologias', sa.String(length=100), nullable=True),
    sa.Column('idiomas', sa.String(length=100), nullable=True),
    sa.Column('bio', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###
