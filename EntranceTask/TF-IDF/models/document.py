from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, func
from .user import metadata
  
documents = Table(
    "documents",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("filename", String, nullable=False),
    Column("path", String, nullable=False),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("uploaded_at", DateTime, default=func.now())
)



# ## 📄 Documents
# Stores metadata for uploaded text files.

# | Field      | Type     | Description                        |
# |------------|----------|------------------------------------|
# | id         | Integer  | Primary key                        |
# | filename   | String   | Original name of uploaded file     |
# | path       | String   | File storage path on server        |
# | user_id    | Integer  | FK to Users.id                     |
# | uploaded_at| DateTime | Upload timestamp                   |

# ---