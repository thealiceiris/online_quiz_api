"""Add total_questions to Results

Revision ID: 2dd4ee1f128a
Revises: 77f189116402
Create Date: 2024-09-28 22:16:58.434028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dd4ee1f128a'
down_revision = '77f189116402'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # Add total_questions column with a default value of 0 for existing rows
    with op.batch_alter_table('results', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_questions', sa.Integer(), nullable=False, server_default='0'))

    # Remove the default value (optional)
    op.alter_column('results', 'total_questions', server_default=None)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('results', schema=None) as batch_op:
        batch_op.drop_column('total_questions')

    # ### end Alembic commands ###
