"""create_users_table

Revision ID: 03b47e787d27
Revises: 
Create Date: 2024-05-07 09:41:31.449562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03b47e787d27'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_name', sa.String(30), primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        schema='public'
    )    


def downgrade() -> None:
    op.drop_table('users', schema='public')
