from pydantic import BaseModel, Field
from datetime import datetime

name_validation = Field(
        ...,
        title="Category Name",
        description="Used for describing the name of the collection",
        max_length=50,
        min_length=5,
        examples="music"
    )


class CreateCollection(BaseModel):
    name : str = name_validation
    user_id : int = Field(
        ...,
        title="User ID",
        description="Used for referencing the user from the db",
        ge=0,
        examples=1
    )

class UpdateCollection(BaseModel):
    name :  str = name_validation
    
    
class CollectionRead(BaseModel):
    id: int = Field(..., title="Collection ID", example=1)
    name: str = Field(..., title="collection name", example="music")
    user_id: int = Field(..., title="user ID", example=1)
    created_at: datetime = Field(..., title="Upload Timestamp", description="Date and time when the document was uploaded")

    
    class Config:
        from_attributes  = True