from fastapi import FastAPI

from app.database.db import Base, engine
from app.routes.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router

app = FastAPI()

app.include_router(auth_router, prefix='/auth')
app.include_router(user_router, prefix='/user')

Base.metadata.create_all(bind=engine)

