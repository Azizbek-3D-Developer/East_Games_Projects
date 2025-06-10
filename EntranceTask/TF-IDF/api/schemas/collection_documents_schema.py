from pydantic import BaseModel, Field

class CollectionDocumentBase(BaseModel):
    collection_id: int = Field(..., title="Collection ID", example=1)
    document_id: int = Field(..., title="Document ID", example=1)


class CollectionDocumentRead(CollectionDocumentBase):
    class Config:
        from_attributes = True
