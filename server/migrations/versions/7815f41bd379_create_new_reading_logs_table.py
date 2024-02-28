"""create new reading logs table

Revision ID: 7815f41bd379
Revises: 32ba2f2fdebe
Create Date: 2024-02-28 18:57:04.017704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7815f41bd379'
down_revision = '32ba2f2fdebe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reading_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('start_data', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_reading_logs_book_id_books')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reading_logs_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reading_logs')
    # ### end Alembic commands ###
