"""Garantit la colonne users.must_change_password (réparation si absente).

Revision ID: 0009_users_must_chg_pwd
Revises: 0008_parents_nin_nullable
Create Date: 2026-04-05
"""

from alembic import op


revision = "0009_users_must_chg_pwd"
down_revision = "0008_parents_nin_nullable"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "ALTER TABLE users ADD COLUMN IF NOT EXISTS must_change_password BOOLEAN NOT NULL DEFAULT false;"
    )


def downgrade() -> None:
    pass
