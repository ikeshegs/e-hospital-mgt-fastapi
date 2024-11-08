"""create staff table fix

Revision ID: 8edc72ecd4dc
Revises: d57293fe5021
Create Date: 2024-11-07 09:38:36.600704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8edc72ecd4dc'
down_revision: Union[str, None] = 'd57293fe5021'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('staff', 'middle_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('staff', 'middle_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
