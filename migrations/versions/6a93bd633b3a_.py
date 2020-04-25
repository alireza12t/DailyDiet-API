"""empty message

Revision ID: 6a93bd633b3a
Revises: 
Create Date: 2020-04-25 11:40:31.221870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a93bd633b3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('FullName', sa.String(), nullable=False),
    sa.Column('Email', sa.String(), nullable=False),
    sa.Column('Password', sa.String(), nullable=False),
    sa.Column('Admin', sa.Boolean(), nullable=False),
    sa.Column('RegisteredOn', sa.DateTime(), nullable=False),
    sa.Column('Confirmed', sa.Boolean(), nullable=False),
    sa.Column('ConfirmedOn', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###