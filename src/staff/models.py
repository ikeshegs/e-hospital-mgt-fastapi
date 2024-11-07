import uuid
import sqlalchemy.dialects.postgresql as pg
from typing import Optional

from sqlmodel import SQLModel, Field, Column
from datetime import datetime


class Staff(SQLModel, table=True):
    __tablename__ = "staff"

    sid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    staff_id: str
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: str
    password: str = Field(exclude=True, min_length=8)
    phone_number: str
    sex: str
    age: int
    is_verified: bool = Field(default=False)
    department: str
    role: str
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )


    def __repr__(self):
        return f"< Staff {self.staff_id}>"
