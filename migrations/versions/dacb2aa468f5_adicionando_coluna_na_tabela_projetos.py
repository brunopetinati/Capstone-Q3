"""adicionando coluna na tabela projetos

Revision ID: dacb2aa468f5
Revises: a7a13732b59c
Create Date: 2021-04-20 02:28:28.338708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dacb2aa468f5'
down_revision = 'a7a13732b59c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projetos', sa.Column('owner_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'projetos', 'usuarios', ['owner_id'], ['email'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'projetos', type_='foreignkey')
    op.drop_column('projetos', 'owner_id')
    # ### end Alembic commands ###