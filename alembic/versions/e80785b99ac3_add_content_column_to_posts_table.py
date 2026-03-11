"""add content column to posts table

Revision ID: e80785b99ac3
Revises: f57fa06fb351
Create Date: 2026-03-10 07:14:54.092109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e80785b99ac3'
down_revision: Union[str, Sequence[str], None] = 'f57fa06fb351'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
