"""create user,article, author models

Revision ID: 53ea07496d12
Revises: 
Create Date: 2023-03-09 14:52:41.687507

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "53ea07496d12"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=80), nullable=False),
        sa.Column("first_name", sa.String(length=120), server_default="", nullable=False),
        sa.Column("last_name", sa.String(length=120), server_default="", nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.Column("is_staff", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("email", name=op.f("uq_users_email")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("fk_authors_user_id_users")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_authors")),
    )
    op.create_table(
        "articles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=80), nullable=True),
        sa.Column("text", sa.Text(), nullable=True),
        sa.Column("dt_created", sa.DateTime(), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=True),
        sa.Column("dt_updated", sa.DateTime(), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["author_id"], ["authors.id"], name=op.f("fk_articles_author_id_authors")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_articles")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("articles")
    op.drop_table("authors")
    op.drop_table("users")
    # ### end Alembic commands ###
