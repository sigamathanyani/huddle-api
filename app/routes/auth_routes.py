from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.user_schema import CreateUser, LoginUser, TokenResponse
from app.services import auth_service

router = APIRouter()

@router.post('/register', response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register_user(data: CreateUser, db: Session = Depends(get_db)):
    return auth_service.register_user(data=data, db=db)

@router.post('/login', response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login_user(data: LoginUser, db: Session = Depends(get_db)):
    return auth_service.login_user(data=data, db=db)
