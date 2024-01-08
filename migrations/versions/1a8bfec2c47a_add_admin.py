"""add admin

Revision ID: 1a8bfec2c47a
Revises: bb019fac04c9
Create Date: 2024-01-09 01:05:45.666328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1a8bfec2c47a"
down_revision: Union[str, None] = "bb019fac04c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "admin_panel_user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("login", sa.String(length=64), nullable=True),
        sa.Column("password", sa.String(length=128), nullable=True),
        sa.Column("token", sa.String(length=512), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("login"),
        sa.UniqueConstraint("token"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("admin_panel_user")
    # ### end Alembic commands ###
