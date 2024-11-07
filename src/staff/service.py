from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from .models import Staff
from .schemas import StaffCreateModel
from .utils import get_random_number, generate_random_password


class StaffService:
    async def get_staff_by_email(email: str, session: AsyncSession):
        statement = select(Staff).where(Staff.email == email)

        result = await session.exec(statement)

        staff_data = result.first()

        return staff_data
    

    async def create_staff(staff_data: StaffCreateModel, session: AsyncSession):
        staff_data_dict = staff_data.model_dump()

        new_staff = Staff(**staff_data_dict)

        password = generate_random_password()
        new_staff.password = password

        '''
        hash staff password
        '''

        random_number = get_random_number()
        new_staff.staff_id = f"EMHS/{random_number}"

        session.add(new_staff)

        await session.commit()

        return new_staff
    

    async def staff_exists(email, session: AsyncSession):
        staff = await StaffService.get_staff_by_email(email, session)

        return True if staff is not None else False
