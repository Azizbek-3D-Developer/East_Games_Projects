from sqlalchemy import Table, Column, Integer, ForeignKey
from .user import metadata

collection_documents = Table(
    "collection_documents",
    metadata,
    Column("collection_id", Integer, ForeignKey("collections.id"), primary_key=True),
    Column("document_id", Integer, ForeignKey("documents.id"), primary_key=True)
)


# ## 🔗 CollectionDocuments
# Links documents to collections (many-to-many relationship).

# | Field         | Type    | Description                        |
# |---------------|---------|------------------------------------|
# | collection_id | Integer | FK to Collections.id               |
# | document_id   | Integer | FK to Documents.id                 |

# ---