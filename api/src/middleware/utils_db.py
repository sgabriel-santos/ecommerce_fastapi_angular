from ast import Str
from ..config.ConfigDB import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from ..config.ConfigDB import DATABASE, engine

# Dependency
async def get_session() -> AsyncSession:
    """ Open the database connection and return a AsyncSession """
    async with async_session() as session:
        yield session