"""first

Revision ID: 651a7fba5e68
Revises: a81d1082d3fe
Create Date: 2024-06-20 16:00:27.972494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '651a7fba5e68'
down_revision: Union[str, None] = 'a81d1082d3fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'author_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('books', 'category_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'category_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('books', 'author_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###