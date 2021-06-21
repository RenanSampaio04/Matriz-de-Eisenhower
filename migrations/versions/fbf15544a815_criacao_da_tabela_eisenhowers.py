"""Criacao da tabela eisenhowers

Revision ID: fbf15544a815
Revises: 00bd7c7be360
Create Date: 2021-06-20 18:03:49.704082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbf15544a815'
down_revision = '00bd7c7be360'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eisenhowers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('eisenhowers')
    # ### end Alembic commands ###