import uuid

from pydantic import BaseModel, Field


class StaffCreateModel(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: str
    password: str = Field(min_length=8)
    phone_no: int
    age: int
    sex: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "middle_name": "Mark",
                "email": "johndoe123@co.com",
                "password": "testpass123",
                "phone_no": 12345678,
                "age": 23,
                "sex": "male"
            }
        }
    }


class StaffModel(BaseModel):
    uid: uuid.uuid4
    staff_id: str
    first_name: str
    last_name: str
    middle_name: str
    email: str
    password: str = Field(exclude=True)
    phone_no: int
    age: int
    sex: str
    is_verified: bool
