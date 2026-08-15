from sqlalchemy.orm import Session

from app.schemas.user_schema import CompleteUserProfile


def complete_profile(data: CompleteUserProfile, db: Session):
    ...