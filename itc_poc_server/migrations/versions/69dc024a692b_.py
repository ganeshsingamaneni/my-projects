"""empty message

Revision ID: 69dc024a692b
Revises: 26ed81d7e525
Create Date: 2019-09-20 10:31:40.258454

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '69dc024a692b'
down_revision = '26ed81d7e525'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('output_time_balance')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('output_time_balance',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('segment_id', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('paper_machine_id', mysql.VARCHAR(length=155), nullable=False),
    sa.Column('profit_center_id', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('sales_category_id', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('product_id', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('nsr_data_id', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('days_required_for_saleable_production', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('createdAt', mysql.DATETIME(), nullable=True),
    sa.Column('updatedAt', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
