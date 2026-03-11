"""add foreign-key to posts table

Revision ID: dfd6ba81e4a5
Revises: 3d9b32472352
Create Date: 2026-03-10 07:36:37.190606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfd6ba81e4a5'
down_revision: Union[str, Sequence[str], None] = '3d9b32472352'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table = "posts", referent_table = "users", local_cols= ['owner_id'], remote_cols = ['id'], ondelete = "CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk', table_name = "posts")
    op.drop_column('posts', 'owner_id')
    pass
