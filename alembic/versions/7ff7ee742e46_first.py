"""first

Revision ID: 7ff7ee742e46
Revises: 651a7fba5e68
Create Date: 2024-06-20 17:06:51.198020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ff7ee742e46'
down_revision: Union[str, None] = '651a7fba5e68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'author_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('books', 'category_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'category_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('books', 'author_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###
