from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from .schemas import StaffModel, StaffCreateModel
from src.database import get_session


staff_router = APIRouter()


@staff_router.post("/create-staff", status_code=status.HTTP_201_CREATED)
async def create_staff(
    staff_data: StaffCreateModel, session: AsyncSession = Depends(get_session)):

    """
    Create staff account using email, first_name, last_name, middle_name, sex, age, and phone number
    params:
        staff_data: StaffCreateModel
    """
    return {
        "message": "Your server is live"
    }
