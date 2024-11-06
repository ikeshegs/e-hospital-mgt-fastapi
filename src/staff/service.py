from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from .models import Staff
from .schemas import StaffCreateModel


class StaffService:
    async def get_staff_by_email(self, email: str, session: AsyncSession):
        statement = select(Staff).where(Staff.email == email)

        result = await session.exec(statement)

        staff_data = result.first()

        return staff_data
    

    async def create_staff(self, staff_data: StaffCreateModel, session: AsyncSession):
        staff_data_dict = staff_data.model_dump()

        new_staff = Staff(**staff_data_dict)

        '''
        hash staff password
        '''

        session.add(new_staff)

        await session.commit()

        return new_staff
