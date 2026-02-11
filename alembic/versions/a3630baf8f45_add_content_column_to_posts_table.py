"""add content column to posts table

Revision ID: a3630baf8f45
Revises: cac70744a1dc
Create Date: 2026-02-10 22:54:10.138167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3630baf8f45'
down_revision: Union[str, Sequence[str], None] = 'cac70744a1dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String,nullable=False))
    pass


def downgrade() :
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
