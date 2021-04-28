"""adicionando coluna na tabela projetos

Revision ID: a7a13732b59c
Revises: ac2e386aef0d
Create Date: 2021-04-20 02:20:46.304582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7a13732b59c'
down_revision = 'ac2e386aef0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('projetos_owner_id_fkey', 'projetos', type_='foreignkey')
    op.create_foreign_key(None, 'projetos', 'usuarios', ['owner_id'], ['email'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'projetos', type_='foreignkey')
    op.create_foreign_key('projetos_owner_id_fkey', 'projetos', 'usuarios', ['owner_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###
