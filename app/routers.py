from fastapi import APIRouter
from typing import Annotated
from random import randint

from sqlalchemy.orm import Session

from .schemas import UserCreate
from .models import User
from .database import get_db



router = APIRouter(
    prefix='/auth',tags=["Auth endpoint"]
)

@router.post('/register')
async def home(user:UserCreate, db:Annotated[Session,get_db]):

    verification_code = randint(100000,999999)

    new_user = User(
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email,
                hashed_password = user.password,
                verification_code = user.ver
            )