from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, func
from .user import metadata

collections = Table(
    "collections",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("created_at", DateTime, default=func.now()) 
)


# ## 📦 Collections
# Groups of documents under a common user.

# | Field      | Type     | Description                        |
# |------------|----------|------------------------------------|
# | id         | Integer  | Primary key                        |
# | name       | String   | Name of the collection             |
# | user_id    | Integer  | FK to Users.id                     |
# | created_at | DateTime | Creation timestamp                 |

# ---