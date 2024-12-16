"""change age to dob in staff table

Revision ID: 7063c07efc87
Revises: e8b50bb4a08b
Create Date: 2024-12-16 13:37:51.374394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '7063c07efc87'
down_revision: Union[str, None] = 'e8b50bb4a08b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff', sa.Column('dob', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.drop_column('staff', 'age')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('staff', 'dob')
    # ### end Alembic commands ###