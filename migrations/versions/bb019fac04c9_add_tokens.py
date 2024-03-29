"""add tokens

Revision ID: bb019fac04c9
Revises: 0e51254f30e8
Create Date: 2024-01-09 00:50:26.622547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bb019fac04c9"
down_revision: Union[str, None] = "0e51254f30e8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users_tokens",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.String(length=64), nullable=True),
        sa.Column("token", sa.String(length=512), nullable=True),
        sa.Column("date_created", sa.DateTime(), nullable=True),
        sa.Column("date_expired", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.user_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("token"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_tokens")
    # ### end Alembic commands ###
