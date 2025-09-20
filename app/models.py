from sqlalchemy import(
    Column,
    String,
    Integer,
    Text,
    ForeignKey,
    Boolean
)

from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String(length=256),nullable = False,unique=True)
    is_active = Column(Boolean,default=False)
    is_verified = Column(Boolean,default=False)
    verification_code = Column(Integer)

    tasks = relationship("Task",back_populates='user')

    @property
    def full_name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        
        else:
            return self.first_name

    def __repr__(self)->str:
        return f"{self.user_id} {self.email} {self.full_name}"


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    descreption = Column(Text)
    user_id = ForeignKey("users.user_id",ondelete="CASCADE")

    user = relationship("User",back_populates='tasks')

    def __repr__(self)->str:
        return f"{self.task_id} {self.title} {self.user.full_name}"