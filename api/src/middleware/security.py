from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from ..schemas.TokenSchema import TokenData
from jose import JWTError, jwt
from datetime import datetime, timedelta
from ..controllers import UserController
from ..middleware.utils_db import get_session
from ..schemas.UserSchema import User

# to get a string like this run on bash prompt:
# openssl rand -hex 32
SECRET_KEY = "70dd049806c1663430a0456c4467be548289a8cb7ce1fcdf3301898ae32e0b0f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", scheme_name="OAuth2PasswordBearer with JWT")

async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await UserController.get_user_by_email(db, email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect email",
        )
    
    if user.password != password:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password",
        )
    
    return user

def create_access_token(user: User):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta

    # to_encode = {"sub": user.name, "exp": expire}
    to_encode = {"sub": user.email}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception

        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
   
    user = await UserController.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user