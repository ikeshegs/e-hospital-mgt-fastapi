import uuid

from datetime import datetime
from pydantic import BaseModel


class CreateStaffScheduleModel(BaseModel):
    start_time: str
    end_time: str
    department: str
    staff_uid: str


class StaffScheduleModel(BaseModel):
    uid: uuid.UUID
    start_time: datetime
    end_time: datetime
    department: str
    created_at: datetime
    updated_at: datetime


class UpdateStaffScheduleModel(BaseModel):
    start_time: str
    end_time: str
