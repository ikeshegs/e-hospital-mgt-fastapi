from __future__ import annotations

import uuid
import sqlalchemy.dialects.postgresql as pg

from datetime import datetime
from sqlmodel import SQLModel, Field, Column, TIMESTAMP, Relationship


class StaffSchedule(SQLModel, table=True):
    __tablename__ = "staff_schedule"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    start_time: datetime = Field(sa_column=Column(TIMESTAMP))
    end_time: datetime = Field(sa_column=Column(TIMESTAMP))
    department: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    staff_uid: uuid.UUID = Field(default=None, foreign_key="staff.uid")

    # staff: "Staff" = Relationship(back_populates="staff_schedule")


from src.staff.models import Staff

StaffSchedule.model_rebuild()