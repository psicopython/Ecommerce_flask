"""empty message

Revision ID: 7d1e050d6592
Revises: 8cfa71e46c2d
Create Date: 2020-09-23 01:08:41.173275

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7d1e050d6592'
down_revision = '8cfa71e46c2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('city', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('state', sa.String(length=64), nullable=False))
    op.drop_column('users', 'cidade')
    op.drop_column('users', 'estado')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('estado', mysql.VARCHAR(length=64), nullable=False))
    op.add_column('users', sa.Column('cidade', mysql.VARCHAR(length=64), nullable=True))
    op.drop_column('users', 'state')
    op.drop_column('users', 'city')
    # ### end Alembic commands ###
