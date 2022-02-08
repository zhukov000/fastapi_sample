from fastapi import Depends, status, HTTPException

from repositories.users import UserRepository
from db.base import database
from core.security import JWTBearer
from models.users import User
from core.security import decode_access_token

def get_user_repository() -> UserRepository:
    return UserRepository(database)


async def get_current_user(
        users: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer()),
    ) -> User:
    credentials_exp = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exp

    email: str = payload.get("sub")
    if email is None:
        raise credentials_exp

    user = await users.get_by_email(email=email)
    if user is None:
        raise credentials_exp

    return user