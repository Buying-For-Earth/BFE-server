"""empty message

Revision ID: 9a75b52f4045
Revises: 835f00f0bfbe
Create Date: 2021-05-03 22:33:25.745505

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9a75b52f4045'
down_revision = '835f00f0bfbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_option', 'input_option')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_option', sa.Column('input_option', mysql.JSON(), nullable=True))
    # ### end Alembic commands ###
