import uuid

from datetime import datetime
from pydantic import BaseModel, Field


class StaffCreateModel(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = ""
    email: str
    phone_number: str
    dob: str
    sex: str
    department: str
    sub_department: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "middle_name": "Mark",
                "email": "johndoe123@co.com",
                "phone_number": "12345678",
                "dob": "23/5/2005",
                "sex": "male",
                "department": "Medical Doctor",
                "sub_department": "Dentist"
            }
        }
    }


class StaffModel(BaseModel):
    uid: uuid.UUID
    staff_id: int
    first_name: str
    last_name: str
    middle_name: str
    email: str
    password: str = Field(exclude=True)
    phone_number: str
    dob: datetime
    sex: str
    is_verified: bool
    is_admin: bool
    department: str
    sub_department: str
    created_at: datetime
    updated_at: datetime


class StaffUpdateModel(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    phone_number: str
    is_admin: bool
    department: str
    sub_department: str
