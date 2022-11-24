"""main tables

Revision ID: fdf8821871d7
Revises:
Create Date: 2019-09-22 01:36:44.791880

"""
from typing import Tuple

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func

revision = "fdf8821871d7"
down_revision = None
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    op.execute(
        """
    CREATE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS
    $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """
    )


def timestamps() -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
            onupdate=func.current_timestamp(),
        ),
    )


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("salt", sa.Text, nullable=False),
        sa.Column("hashed_password", sa.Text),
        sa.Column("name", sa.Text),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_user_modtime
            BEFORE UPDATE
            ON users
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_operation_table() -> None:
    op.create_table(
        "operation",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("sess_id", sa.Text, unique=True, nullable=False, index=True),
        sa.Column(
            "author_id", sa.Integer, sa.ForeignKey("users.id", ondelete="SET NULL")
        ),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_operation_modtime
            BEFORE UPDATE
            ON operation
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_entry_table() -> None:
    op.create_table(
        "entry",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("info", sa.Text),
        sa.Column(
            "op_id", sa.Integer, sa.ForeignKey("operation.id", ondelete="SET NULL")
        ),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_collection_modtime
            BEFORE UPDATE
            ON entry
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_updated_at_trigger()
    create_users_table()
    create_operation_table()
    create_entry_table()


def downgrade() -> None:
    op.drop_table("entry")
    op.drop_table("operation")
    op.drop_table("users")
    op.execute("DROP FUNCTION update_updated_at_column")
