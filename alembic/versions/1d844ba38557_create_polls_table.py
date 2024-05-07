"""create_polls_table

Revision ID: 1d844ba38557
Revises: 03b47e787d27
Create Date: 2024-05-07 09:45:56.133990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import enum
class PollType(enum.Enum):
    text = 1
    image = 2

# revision identifiers, used by Alembic.
revision: str = '1d844ba38557'
down_revision: Union[str, None] = '03b47e787d27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'polls',
        sa.Column('title', sa.String(255), primary_key=True),
        sa.Column('type', sa.Enum(PollType), nullable=False),
        sa.Column('is_add_choices_active', sa.Boolean, nullable=False),
        sa.Column('is_voting_active', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        schema='public'
    )

def downgrade() -> None:
    op.drop_table('polls')
