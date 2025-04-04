from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    email: str
    name: str
    

class UserCreationSchmea(BaseUser):
    password: str = Field(..., min_length=8, max_length=120)
    

class UserRetriveSchema(BaseUser):
    is_active: bool
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "user@example.com",
                "name": "John Doe",
                "is_active": True,
            }
        }
    