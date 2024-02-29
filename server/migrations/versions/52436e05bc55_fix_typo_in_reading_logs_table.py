"""fix typo in reading logs table

Revision ID: 52436e05bc55
Revises: a971432f51f9
Create Date: 2024-02-28 19:04:20.378465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52436e05bc55'
down_revision = 'a971432f51f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reading_logs', 'end_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reading_logs', sa.Column('end_date', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###