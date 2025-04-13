from sqlalchemy import (Column, String, Integer,
                        Text, ForeignKey, DateTime, Boolean)
from sqlalchemy.orm import relationship
from db.base import Base
from datetime import datetime


class Post(Base):
    """
    The main Post model
    """
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(String(255), nullable=False)
    
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(
    Integer,
    ForeignKey("categories.id", ondelete="SET NULL"),
    nullable=True
    )
    
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    is_published = Column(Boolean, default=True)
    
    author = relationship("User", back_populates="posts")
    category = relationship("Category", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Post(title='{self.title}', author_id={self.author_id})>"
    