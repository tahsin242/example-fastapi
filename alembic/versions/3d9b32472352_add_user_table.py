"""add user table

Revision ID: 3d9b32472352
Revises: e80785b99ac3
Create Date: 2026-03-10 07:30:50.938926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d9b32472352'
down_revision: Union[str, Sequence[str], None] = 'e80785b99ac3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable = False),
                    sa.Column('email', sa.String(), nullable = False), 
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone = True),
                              server_default = sa.text('now()'), nullable = False),
                              sa.PrimaryKeyConstraint('id'),
                              sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
