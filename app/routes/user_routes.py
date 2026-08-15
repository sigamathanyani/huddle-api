from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.dependencies.user_dependency import get_current_user
from app.schemas.user_schema import (
    CompleteUserProfile,
    Temp,
    UserCompleteProfileResponse,
    UserResponse,
)
from app.services import user_service

router = APIRouter()


@router.get("/me", response_model=Temp)
def me(user: dict = Depends(get_current_user)):
    return user


@router.put(
    "/complete-profile",
    response_model=UserCompleteProfileResponse,
    status_code=status.HTTP_200_OK,
)
def cmplete_user_profile(data: CompleteUserProfile, db: Session = Depends(get_db)):
    return user_service.complete_profile(data=data, db=db)
