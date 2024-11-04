from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from src.config import Config


engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True,
        future=True
    )
)


async def init_db() -> None:
    async with engine.begin() as conn:
        
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    
    Session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
