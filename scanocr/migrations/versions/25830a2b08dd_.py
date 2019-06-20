"""empty message

Revision ID: 25830a2b08dd
Revises: 
Create Date: 2018-12-04 12:27:02.004412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25830a2b08dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permission', sa.Column('client_viewname', sa.String(length=50), nullable=True))
    op.add_column('permission', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('permission', sa.Column('status', sa.Boolean(), nullable=True))
    op.add_column('permission', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('permission', 'updated_at')
    op.drop_column('permission', 'status')
    op.drop_column('permission', 'created_at')
    op.drop_column('permission', 'client_viewname')
    # ### end Alembic commands ###
