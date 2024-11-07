from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from .schemas import StaffModel, StaffCreateModel
from src.database import get_session
from .service import StaffService


staff_router = APIRouter()
staff_service = StaffService


@staff_router.post("/create-staff", status_code=status.HTTP_201_CREATED)
async def create_staff(
    staff_data: StaffCreateModel, session: AsyncSession = Depends(get_session)):

    """
    Create staff account using email, first_name, last_name, middle_name, sex, age, and phone number
    params:
        staff_data: StaffCreateModel
    """

    staff_email = staff_data.email

    staff_exists = await staff_service.staff_exists(staff_email, session)

    if staff_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
    
    new_staff_account = await staff_service.create_staff(staff_data, session)

    return {
        "message": f"The account belonging to {staff_data.first_name} has been created",
        "user": new_staff_account
    }
