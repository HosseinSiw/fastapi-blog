from pydantic import BaseModel, ConfigDict


# preventing import the BaseClass on other modules
__all__ = ["CategoryRetriveSchema", "CategoryCreationSchema"]  


class CategoryBaseSchema(BaseModel):
    name: str
    
    
class CategoryRetriveSchema(CategoryBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "name": "Technology",
            "id": 1,
        }
    })
    
class CategoryCreationSchema(CategoryBaseSchema):
    pass
