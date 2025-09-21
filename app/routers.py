from fastapi import APIRouter,Depends
from typing import Annotated
from random import randint

from sqlalchemy.orm import Session

from fastapi_mail import FastMail,MessageSchema

from .schemas import UserCreate
from .models import User
from .database import get_db
from .config import mail_conf

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



router = APIRouter(
    prefix='/auth',tags=["Auth endpoint"]
)

@router.post('/register')
async def home(user:UserCreate, db:Annotated[Session,Depends(get_db)]):

    hashed_password = pwd_context.hash(user.password)
    verification_code = randint(100000,999999)

    new_user = User(
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email,
                hashed_password = hashed_password,
                verification_code = verification_code
            )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    
    message = MessageSchema(
            subject="FastAPI Mail Test",
            recipients=[user.email],
            body=f"Tasdiqlash kod: {verification_code}",
            subtype="plain"
        )
    
    fm = FastMail(mail_conf)

    await fm.send_message(
        message
    )

    return {
        "message":"succes"
    }