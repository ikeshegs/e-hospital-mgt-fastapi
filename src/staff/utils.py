import random
import string

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from passlib.context import CryptContext

from .models import Staff


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


def verify_password_hash(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


async def staff_id_exists(staff_id: int, session: AsyncSession) -> bool:
    statement = select(Staff.staff_id).where(Staff.staff_id == staff_id)

    result = await session.exec(statement)

    id = result.first()

    return True if id else False


def get_random_number() -> int:
    random_number = random.randint(1, 9999)
    return random_number


def generate_random_password() -> str:
    '''
    Generates a random password having the specified length
    :returns a string>
    '''

    LETTERS = string.ascii_letters
    NUMBERS = string.digits

    password_length: int = 8
    
    alphanumeric = f"{LETTERS}{NUMBERS}"

    # convert alphanumeric from string to list and shuffle
    alphanumeric = list(alphanumeric)
    random.shuffle(alphanumeric)

    # generate random password and convert to string
    random_password = random.choices(alphanumeric, k=password_length)
    random_password = ''.join(random_password)
    return random_password
