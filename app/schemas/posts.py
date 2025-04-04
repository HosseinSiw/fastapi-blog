from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

# Post base, shared information within all HTTP methods
class PostBase(BaseModel):
    title: str
    content: str
    summary: str
    
    model_config = ConfigDict(from_attributes=True)


# GET Method schemas
class UserPost(BaseModel):
    id: int
    email: EmailStr
    name: str
    model_config = ConfigDict(from_attributes=True)
    
# Get method 2
class PostRetriveSchema(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: datetime
    author: UserPost 
    
    model_config = ConfigDict(from_attributes=True)   


# Post method, for creating posts 
class PostCreationSchema(PostBase):
    pass

# PATCH method.
class PostUpdateSchema(BaseModel):
    title: str | None = None
    content: str | None = None
    summary: str | None = None
    is_published: bool | None = None
    
    model_config = ConfigDict(from_attributes=True)
