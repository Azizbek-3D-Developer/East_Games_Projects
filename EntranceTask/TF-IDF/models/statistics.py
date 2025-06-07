from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, JSON, func
from .user import metadata

statistics = Table(
    "statistics",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("document_id", Integer, ForeignKey("documents.id"), nullable=False),
    Column("tfidf_json", JSON),
    Column("created_at", DateTime, default=func.now()) 
)


# ## 📊 Statistics
# Stores TF-IDF results for a document or aggregated per collection.

# | Field         | Type     | Description                           |
# |---------------|----------|---------------------------------------|
# | id            | Integer  | Primary key                           |
# | document_id   | Integer  | FK to Documents.id                    |
# | tfidf_json    | JSON     | List of top 50 words with TF and IDF  |
# | created_at    | DateTime | When stats were computed              |

# ---