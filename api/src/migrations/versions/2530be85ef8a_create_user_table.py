"""create user table

Revision ID: 2530be85ef8a
Revises: 
Create Date: 2023-10-24 19:18:28.040523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2530be85ef8a'
down_revision = None
branch_labels = None
depends_on = None

table_name = 'user'

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table(table_name)
