from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.user_model import UserTable
from app.utils.jwt import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    access_token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> UserTable:
    user_data = decode_token(token=access_token)
    user_id = user_data.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Something went wrong please log in again",
        )

    user = db.query(UserTable).filter(UserTable.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User was not found please log in",
        )

    return user
