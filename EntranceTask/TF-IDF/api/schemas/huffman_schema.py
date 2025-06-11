from typing import List
from datetime import datetime
from pydantic import BaseModel, Field

# 🧠 Reusable field definitions
user_id_field = Field(
    ...,
    title="User ID",
    description="The ID of the user who owns this Huffman encoding",
    ge=1,
    example=1
)

document_id_field = Field(
    ...,
    title="Document ID",
    description="The ID of the document for which this Huffman encoding was generated",
    ge=1,
    example=10
)

letter_field = Field(
    ...,
    title="Character",
    description="A single character from the document that was encoded (can include whitespace like space, newline, etc.)",
    min_length=1,
    max_length=15,
    example="e"
)

code_field = Field(
    ...,
    title="Huffman Code",
    description="The binary Huffman code assigned to the character",
    example="101"
)

# 🧩 Individual Huffman code pair
class HuffmanPair(BaseModel):
    letter: str = letter_field  # must be actual character, not '[space]' etc.
    code: str = code_field

# 📦 Base schema used by create/update/read
class HuffmanBase(BaseModel):
    user_id: int = user_id_field
    document_id: int = document_id_field
    pairs: List[HuffmanPair] = Field(
        ...,
        title="Huffman Encoded Pairs",
        description="List of characters and their corresponding Huffman codes"
    )

# 🆕 Create
class HuffmanCreate(HuffmanBase):
    pass

# ✏️ Update (same fields as create)
class HuffmanUpdate(HuffmanBase):
    pass

# 📖 Read
class HuffmanRead(HuffmanBase):
    id: int = Field(
        ...,
        title="Encoding ID",
        description="The unique ID of the Huffman encoding entry",
        example=100
    )
    created_at: datetime = Field(
        ...,
        title="Creation Timestamp",
        description="The timestamp when this encoding was generated"
    )

    class Config:
        from_attributes = True
