from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from .schemas import StaffScheduleModel, CreateStaffScheduleModel
from .service import StaffScheduleService
from src.database import get_session


staff_schedule_router = APIRouter()
staff_schedule_service = StaffScheduleService


@staff_schedule_router.post("/create-staff-schedule", status_code=status.HTTP_201_CREATED)
async def create_staff_schedule(staff_schedule_data: CreateStaffScheduleModel, session: AsyncSession = Depends(get_session)):

    new_staff_schedule = await staff_schedule_service.create_staff_schedule(staff_schedule_data, session)

    if new_staff_schedule is not None:
        return {
            "message": f"Staff Schedule for {new_staff_schedule.staff_uid}, in {new_staff_schedule.department} has been created successfully",
            "schedule": new_staff_schedule
        }
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating staff schedule")
