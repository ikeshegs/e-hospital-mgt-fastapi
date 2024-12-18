from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.responses import JSONResponse

from .schemas import StaffModel, StaffCreateModel, StaffUpdateModel
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


@staff_router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_staffs(session: AsyncSession = Depends(get_session)):
    all_staffs = await staff_service.get_all_staff(session)

    return all_staffs


@staff_router.get("/{department_name}")
async def get_all_department_staff(department_name: str, session: AsyncSession = Depends(get_session)):
    staffs_in_department = await staff_service.get_all_staffs_in_a_department(department_name, session)

    if staffs_in_department is None:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Sorry, no staff in this department yet."
            }
        )
    else:    
        return staffs_in_department


@staff_router.get("/sid/{staff_uid}", response_model=StaffModel)
async def get_staff(staff_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    staff = await staff_service.get_staff(staff_uid, session)

    return staff


@staff_router.patch("/sid/{staff_uid}", response_model=StaffModel)
async def update_staff(
    staff_uid: str, 
    staff_update_data: StaffUpdateModel,  
    session: AsyncSession = Depends(get_session)
) -> dict:
    
    updated_staff = await staff_service.update_staff(staff_uid, staff_update_data, session)

    if updated_staff is None:
        raise HTTPException(detail="Staff not found", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return updated_staff
