from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from ..repository import UserRepository
from ..schemas import UserSchema


# CREATE operations
async def create_user(db: AsyncSession, user: UserSchema.UserCreate):
    db_user = await UserRepository.get_user_by_email(db, user.email)
    
    if db_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    
    try:
        await UserRepository.create_user(db, user=user)
        await db.commit()
        return True
    
    except:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Server Error")

# READ operations
async def get_users(db: AsyncSession):
    return await UserRepository.get_users(db)

async def get_user_by_id(db: AsyncSession, user_id: int):
    db_user = await UserRepository.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
    return db_user

async def get_user_by_email(db: AsyncSession, email: str):
    db_user = await UserRepository.get_user_by_email(db, email)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not Found")
    return db_user


# UPDATE operations
async def update_user(db: AsyncSession, user: UserSchema.UserCreate, user_id: int):
    db_user = await UserRepository.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    try:
        await UserRepository.update_user(db, user=user, user_id=user_id)
        await db.commit()
        return True
    except:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Server Error")


# DELETE operations
async def delete_user(db: AsyncSession, user_id: int, current_user_id: int):
    db_user = await UserRepository.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    try:
        await UserRepository.delete_user(db, user_id=user_id)
        await db.commit()
        return db_user
    except:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Server Error")
