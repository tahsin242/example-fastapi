"""add last few columns to posts table

Revision ID: d44465662017
Revises: dfd6ba81e4a5
Create Date: 2026-03-10 07:44:00.568434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd44465662017'
down_revision: Union[str, Sequence[str], None] = 'dfd6ba81e4a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published', sa.Boolean(), nullable = False, server_default = 'TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('NOW()')),)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
