from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from db.base import Base


class User(Base):
    """
    The main user model.
    """
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String,)
    email: str = Column(String, unique=True)
    password: str = Column(String,)
    is_active: bool = Column(Boolean, default=True)
    is_superuser: bool = Column(Boolean, default=False)
    
    posts = relationship("Post", back_populates="author", cascade="all, delete")