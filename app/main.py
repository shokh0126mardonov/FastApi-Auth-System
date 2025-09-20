from fastapi import FastAPI

from .database import Base,engine
from .models import User,Task

Base.metadata.create_all(engine)

app = FastAPI(title="Auth System")

@app.get('/')
async def root():
    return {
        "message":"Hello world"
    }