"""empty message

Revision ID: 73478de07715
Revises: 868388f53cfe
Create Date: 2021-05-02 19:44:24.960045

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '73478de07715'
down_revision = '868388f53cfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'detail',
               existing_type=mysql.JSON(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'detail',
               existing_type=mysql.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
