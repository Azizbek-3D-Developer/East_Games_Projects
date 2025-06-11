from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, JSON
from sqlalchemy.sql import func
from models.user import metadata 

huffman_encodings = Table(
    "huffman_encodings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("document_id", Integer, ForeignKey("documents.id", ondelete="CASCADE"), nullable=False),
    Column("pairs", JSON, nullable=False),  # Stores [{"letter": "a", "code": "101"}, ...]
    Column("created_at", DateTime, default=func.now())
)


# ##  📊 Huffman
# | Field        | Type     | Description                              |
# | ------------ | -------- | ---------------------------------------- |
# | id           | Integer  | Primary key                              |
# | user_id      | Integer  | FK to Users.id                           |
# | document_id  | Integer  | FK to Documents.id                       |
# | pairs        | JSON     | Huffman encoding pairs: letter/code list |
# | created_at   | DateTime | Timestamp when the encoding was created  |
