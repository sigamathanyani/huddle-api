from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.settings.config import get_setting

engine: Engine = create_engine(get_setting().database_url)

SessionLocal = sessionmaker(autocommit=False ,autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()