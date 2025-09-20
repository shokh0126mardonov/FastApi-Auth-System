from sqlalchemy import(
    Column,
    String,
    Integer,
    Text,
    ForeignKey
)

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)