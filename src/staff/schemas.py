import uuid

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
    role: str

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
                "role": "Dentist"
            }
        }
    }


class StaffModel(BaseModel):
    uid: uuid.uuid5
    staff_id: int
    first_name: str
    last_name: str
    middle_name: str
    email: str
    password: str = Field(exclude=True)
    phone_no: str
    dob: str
    sex: str
    is_verified: bool
    is_admin: bool
    department: str
    role: str
