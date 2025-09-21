from fastapi import FastAPI

from .database import Base,engine
from .models import User,Task
from .routers import router

Base.metadata.create_all(engine)

app = FastAPI(title="Auth System",description="Emailga message jonatish")

app.include_router(router)

@app.get('/')
async def root():
    return {
        "message":"Hello world"
    }