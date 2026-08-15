from typing import cast

from fastapi import Depends, HTTPException, status

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.user_model import UserTable
from app.schemas.user_schema import CreateUser, LoginUser, TokenResponse
from app.utils.security import hash_password, verify_hash
from app.utils.jwt import generate_token


def register_user(data: CreateUser, db: Session = Depends(get_db)) -> TokenResponse:
    # Check if the email or the username already exist in the db
    existing_user = (
        db.query(UserTable)
        .filter(or_(UserTable.email == data.email, UserTable.username == data.username))
        .first()
    )

    # If exist throw an error
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exist",
        )

    # If not hash the password
    hashed_password = hash_password(data.plain_password)

    user_to_save = UserTable(
        email=data.email,
        username=data.username,
        hashed_password=hashed_password,
        profile_picture=data.profile_picture,
    )

    # save the user in the db
    db.add(user_to_save)
    db.commit()
    db.refresh(user_to_save)
    payload = {"user_id": user_to_save.id}
    access_token = generate_token(payload=payload, token_type="access_token")
    return TokenResponse(access_token=access_token)


def login_user(data: LoginUser, db: Session) -> TokenResponse:

    existing_user = (
        db.query(UserTable)
        .filter(UserTable.email == data.email, UserTable.username == data.username)
        .first()
    )

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password is incorrect, please verify",
        )
    # check if the password matches
    password_is_match = verify_hash(data.plain_password, existing_user.hashed_password)

    # if password do not match -> raise http exception
    if not password_is_match:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password is incorrect, please verify",
        )

    payload = {"user_id": existing_user.id}

    access_token = generate_token(payload=payload, token_type="access_token")

    # if password match -> generate a token
    return TokenResponse(access_token=access_token)
