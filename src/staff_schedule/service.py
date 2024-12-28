from sqlmodel.ext.asyncio.session import AsyncSession

from .models import StaffSchedule
from .schemas import CreateStaffScheduleModel
from src.utils import convert_string_to_datetime


class StaffScheduleService:

    async def create_staff_schedule(staff_schedule_data: CreateStaffScheduleModel, session: AsyncSession):
        
        staff_schedule_data_dict = staff_schedule_data.model_dump()

        new_staff_schedule = StaffSchedule(**staff_schedule_data_dict)

        # convert 'start_time' & 'end_time' string to DateTime object
        new_staff_schedule.start_time = convert_string_to_datetime(new_staff_schedule.start_time)
        new_staff_schedule.end_time = convert_string_to_datetime(new_staff_schedule.end_time)

        session.add(new_staff_schedule)

        await session.commit()

        return new_staff_schedule
