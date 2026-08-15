from datetime import datetime

from sqlalchemy import DateTime, String, Column, Integer

from app.utils.constants import LONG_LENGTH, SHORT_LENGTH
from app.database.db import Base

class UserTable(Base):

    __tablename__ = 'users'

    id              = Column(Integer, primary_key=True, autoincrement=True)
    email           = Column(String(SHORT_LENGTH), nullable=False, unique=True)
    username        = Column(String(SHORT_LENGTH), nullable=False, unique=True)
    hashed_password = Column(String(LONG_LENGTH), nullable=False)
    name            = Column(String(SHORT_LENGTH))
    surname         = Column(String(SHORT_LENGTH))
    phone_number    = Column(String(SHORT_LENGTH))
    gender          = Column(String(SHORT_LENGTH))
    profile_picture = Column(String(LONG_LENGTH))
    created_at      = Column(DateTime, nullable=False, default=datetime.now)