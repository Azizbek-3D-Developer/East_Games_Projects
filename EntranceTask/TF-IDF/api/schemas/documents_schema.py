from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class DocumentBase(BaseModel):
    filename: str = Field(..., description="Original name of the uploaded file")
    path: str = Field(..., description="Server file path where the uploaded file is stored")
    user_id: int = Field(..., description="ID of the user who uploaded the file", examples={"user_id": 1})


class DocumentCreate(DocumentBase):
    """Schema for creating a new document"""
    pass


class DocumentUpdate(BaseModel):
    """Schema for updating an existing document"""
    filename: Optional[str] = Field(None, description="Updated file name")
    path: Optional[str] = Field(None, description="Updated file path")


class DocumentRead(DocumentBase):
    """Schema for reading a document (response model)"""
    id: int = Field(..., description="Unique document ID")
    uploaded_at: datetime = Field(..., description="Timestamp when the document was uploaded")

    class Config:
        from_attributes = True  
