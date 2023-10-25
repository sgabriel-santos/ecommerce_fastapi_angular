from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import UserSchema
from ..models import UserModel
from sqlalchemy.future import select
from sqlalchemy import update, delete, insert, or_


# CREATE operations
async def create_user(db: AsyncSession, user: UserSchema.UserCreate):
    db_user = await db.execute(insert(UserModel.User).values(user.__dict__))
    return db_user


# READ operations
async def get_users(db: AsyncSession):
    response = await db.execute(select(UserModel.User))
    return response.scalars().all()

async def get_user_by_id(db: AsyncSession, user_id: int):
    response = await db.execute(select(UserModel.User).where(UserModel.User.id == user_id))
    return response.scalars().first()

async def get_user_by_name(db: AsyncSession, user_name: str):
    response = await db.execute(select(UserModel.User).where(UserModel.User.name == user_name))
    return response.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    response = await db.execute(select(UserModel.User).where(UserModel.User.email == email))
    return response.scalars().first()

# UPDATE operations
async def update_user(db: AsyncSession, user: UserSchema.UserCreate, user_id: int):
    response = await db.execute(update(UserModel.User).where(UserModel.User.id == user_id).values(user.__dict__))
    return response

async def update_user_outsourced(db: AsyncSession, user: UserSchema.UserCreate, user_id: int):
    response = await db.execute(update(UserModel.User).where(UserModel.User.id == user_id).values(user.__dict__))
    return response


# DELETE operations
async def delete_user(db: AsyncSession, user_id: int):
    response = await db.execute(delete(UserModel.User).where(UserModel.User.id == user_id))
    return response
