# imports
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.schema import MetaData

# This metaData will be used in other models also
metadata = MetaData()

# users table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, unique=True, nullable=False),
    Column("username", String, unique=True, nullable=False),
    Column("password_hash", String, nullable=False),
    Column("created_at", DateTime, default=func.now())
)

# ## 👤 Users
# Stores system users who can upload and manage documents and collections.
# | Field         | Type     | Description                     |
# |---------------|----------|---------------------------------|
# | id            | Integer  | Primary key                     |
# | email         | String   | Unique eamil                    |
# | username      | String   | Unique username                 |
# | password_hash | String   | Hashed password                 |
# | created_at    | DateTime | Account creation timestamp      |
