from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime


# Post base, shared information within all HTTP methods
class PostBase(BaseModel):
    title: str = Field(..., max_length=255, description="Post title")
    content: str = Field(..., max_length=255, description="Post content")
    summary: str = Field(..., max_length=255, description="a short summary of post content")
    
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
    category_name: str
    model_config = ConfigDict(from_attributes=True)   

# Post method, for creating posts 
class PostCreationSchema(PostBase):
    category_name: str
    is_published: bool = True
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "title": "How AI is Changing Coding",
                "content": "Lots of cool things...",
                "summary": "An overview of AI's impact on dev life.",
                "category_name": "technology"
            }
        }
    )
    

# PATCH method.
class PostUpdateSchema(BaseModel):
    title: str | None = None
    content: str | None = None
    summary: str | None = None
    is_published: bool | None = None
    category_name: str | None = None
    model_config = ConfigDict(from_attributes=True)
