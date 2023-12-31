"""init

Revision ID: 191577bd6d5b
Revises: 
Create Date: 2023-12-31 22:26:07.564583

"""
import sqlalchemy as sa
import sqlmodel  # NEW
from alembic import op

# revision identifiers, used by Alembic.
revision = "191577bd6d5b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "auth_user",
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("password", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("is_admin", sa.Boolean(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_auth_user_email"), "auth_user", ["email"], unique=True)
    op.create_index(op.f("ix_auth_user_id"), "auth_user", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_auth_user_id"), table_name="auth_user")
    op.drop_index(op.f("ix_auth_user_email"), table_name="auth_user")
    op.drop_table("auth_user")
    # ### end Alembic commands ###