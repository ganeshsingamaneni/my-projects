"""empty message

Revision ID: 26ed81d7e525
Revises: 
Create Date: 2019-09-16 18:00:58.100612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26ed81d7e525'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('uom_master', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('uom_master', 'status')
    # ### end Alembic commands ###
