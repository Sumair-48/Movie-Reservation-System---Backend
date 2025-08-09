"""Add auto increamemt

Revision ID: 48abde8e0b9c
Revises: 0cac8315efdc
Create Date: 2025-08-09 13:18:29.490040

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48abde8e0b9c'
down_revision: Union[str, Sequence[str], None] = '0cac8315efdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute('CREATE SEQUENCE user_table_id_seq OWNED BY "User_table"."ID"')

    # Set default value to use the sequence
    op.execute('ALTER TABLE "User_table" ALTER COLUMN "ID" SET DEFAULT nextval(\'user_table_id_seq\')')


def downgrade() -> None:
    """Downgrade schema."""
    pass
