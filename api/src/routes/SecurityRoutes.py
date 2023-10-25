from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from ..middleware.utils_db import get_session
from ..middleware.security import create_access_token,authenticate_user
from ..schemas.TokenSchema import Token

router = APIRouter(tags=["user"])

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    """
    Grants application access to a user if the credentials are correct

    Parameters:
    -------
    **email** (str): User email.\n
    **password** (str): User password.\n

    Returns:
    -------
    A access token to the FontEnd. The Token has a time to expire.
    """
    user = await authenticate_user(db, form_data.username, form_data.password)
    access_token = create_access_token(user)

    return Token(access_token=access_token, token_type="bearer")

    
