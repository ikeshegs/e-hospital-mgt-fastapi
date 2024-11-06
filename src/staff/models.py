import uuid
import sqlalchemy.dialects.postgresql as pg

from sqlmodel import SQLModel, Field, Column
from datetime import datetime


class Staff(SQLModel, table=True):
    __tablename__="staff"

    uid: uuid.uuid5 = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default_factory=uuid.uuid5
        )
    )
    staff_id: str
    first_name: str
    middle_name: str
    last_name: str
    email: str
    password: str = Field(exclude=True)
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
