"""Initial migration

Revision ID: a923b5e30061
Revises: 
Create Date: 2024-09-24 05:25:16.394528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a923b5e30061'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('quizzes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('options', sa.String(length=80), nullable=False),
    sa.Column('answer', sa.String(length=80), nullable=False),
    sa.Column('text', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizzes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizzes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('questions')
    op.drop_table('quizzes')
    op.drop_table('user')
    # ### end Alembic commands ###
