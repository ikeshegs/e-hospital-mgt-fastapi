from datetime import datetime
from sqlmodel.ext.asyncio.session import AsyncSession

from .models import StaffSchedule
from .schemas import (
    StaffScheduleModel, 
    CreateStaffScheduleModel, 
    UpdateStaffScheduleModel
)
from src.staff.service import StaffService


class StaffScheduleService:

    async def create_staff_schedule(staff_schedule_data: CreateStaffScheduleModel, session: AsyncSession):
        
        staff_schedule_data_dict = staff_schedule_data.model_dump()

        new_staff_schedule = StaffSchedule(**staff_schedule_data_dict)

        # convert 'start_time' & 'end_time' string to DateTime object
        new_start_time = datetime.strptime(new_staff_schedule.start_time, '%d/%m/%Y %H:%M:%S')
        new_staff_schedule.start_time = new_start_time

        new_end_time = datetime.strptime(new_staff_schedule.end_time, '%d/%m/%Y %H:%M:%S')
        new_staff_schedule.end_time = new_end_time
        print(f"Debugging........ {new_staff_schedule}")

        session.add(new_staff_schedule)

        await session.commit()

        return new_staff_schedule
