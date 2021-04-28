"""criando tabela solicitacoes

Revision ID: f18e1920e4f5
Revises: 76ada4f52ae0
Create Date: 2021-04-20 03:09:05.505531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f18e1920e4f5'
down_revision = '76ada4f52ae0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solicitacoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('projeto_id', sa.Integer(), nullable=True),
    sa.Column('solicitante', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['projeto_id'], ['projetos.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['solicitante'], ['token.user'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('token', sa.Column('token', sa.Integer(), nullable=False))
    op.add_column('token', sa.Column('user', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'token', ['user'])
    op.create_unique_constraint(None, 'token', ['token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'token', type_='unique')
    op.drop_constraint(None, 'token', type_='unique')
    op.drop_column('token', 'user')
    op.drop_column('token', 'token')
    op.drop_table('solicitacoes')
    # ### end Alembic commands ###