"""add foreign key to post table

Revision ID: d516efc31b43
Revises: ba32600ede87
Create Date: 2026-02-11 01:06:54.795888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd516efc31b43'
down_revision: Union[str, Sequence[str], None] = 'ba32600ede87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    """Upgrade schema."""
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('posts_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
