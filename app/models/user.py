from sqlalchemy import Column, Integer, String, Boolean
from db.base import Base


class User(Base):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String,)
    email: str = Column(String, unique=True)
    password: str = Column(String,)
    is_active: bool = Column(Boolean, default=True)
    is_superuser: bool = Column(Boolean, default=False)
    