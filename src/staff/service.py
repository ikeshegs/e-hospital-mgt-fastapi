from datetime import datetime
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import desc, select

from .models import Staff
from .schemas import StaffCreateModel, StaffUpdateModel
from .utils import get_random_number, generate_random_password, get_password_hash


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

        # hash password
        hashed_password = get_password_hash(password)
        new_staff.password = hashed_password

        # convert string to lowercase
        lowercase_department = new_staff.department.lower()
        new_staff.department = lowercase_department

        lowercase_sub_department = new_staff.sub_department.lower()
        new_staff.sub_department = lowercase_sub_department

        # convert DOB string to DateTime object
        new_dob = datetime.strptime(new_staff.dob, '%d/%m/%Y').date()
        new_staff.dob = new_dob

        '''
        Write a loop/function to ensure that the same random number doesn't get assigned to multiple staffs
        '''
        random_number = get_random_number()
        new_staff.staff_id = random_number

        session.add(new_staff)

        await session.commit()

        return new_staff
    

    async def staff_exists(email, session: AsyncSession):
        staff = await StaffService.get_staff_by_email(email, session)

        return True if staff is not None else False
    

    async def get_all_staff(session: AsyncSession):
        statement = select(Staff).limit(10)

        result = await session.exec(statement)

        return result.all()
    

    async def get_staff(staff_uid: str, session: AsyncSession):
        statement = select(Staff).where(Staff.uid == staff_uid)

        result = await session.exec(statement)

        staff = result.first()

        return staff if staff is not None else None


    async def get_all_staffs_in_a_department(department_name: str, session: AsyncSession):
        lowercase_department_name = department_name.lower()
        statement = select(Staff).where(Staff.department == lowercase_department_name)

        result = await session.exec(statement)

        all_department_staffs = result.all()

        if len(all_department_staffs) == 0:
            return None
        else:
            return all_department_staffs
        

    async def update_staff(
            staff_uid: str, update_data: StaffUpdateModel, session: AsyncSession):
        
        staff_to_update = await StaffService.get_staff(staff_uid, session)

        if staff_to_update is not None:
            staff_update_data_dict = update_data.model_dump()

            for key, value in staff_update_data_dict.items():
                setattr(staff_to_update, key, value)

            staff_to_update.updated_at = datetime.now()

            await session.commit()

            return staff_to_update
        else:
            return None
        

    async def delete_staff(staff_uid, session: AsyncSession):
        staff_to_delete = await StaffService.get_staff(staff_uid, session)

        if staff_to_delete is not None:
            await session.delete(staff_to_delete)

            await session.commit()
            
            return {}
        else:
            return None
