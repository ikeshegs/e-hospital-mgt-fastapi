"""staff table middle_name optional fix

Revision ID: 3db241e6fa7a
Revises: 8332a1eeed21
Create Date: 2024-11-07 10:36:44.497285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3db241e6fa7a'
down_revision: Union[str, None] = '8332a1eeed21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
