"""trocando unique para true em token.token

Revision ID: fae68409505d
Revises: 7b001f135efa
Create Date: 2021-04-20 02:56:27.353608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fae68409505d'
down_revision = '7b001f135efa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solicitacoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('projeto_id', sa.Integer(), nullable=True),
    sa.Column('solicitante', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['projeto_id'], ['projetos.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['solicitante'], ['token.nome'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('token', sa.Column('token', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'token', ['token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'token', type_='unique')
    op.drop_column('token', 'token')
    op.drop_table('solicitacoes')
    # ### end Alembic commands ###