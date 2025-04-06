from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, default='default')
    
    posts = relationship("Post", back_populates="category")
