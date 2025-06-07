import os
from databases import Database
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tfidf.db")
DATABASE_URL = os.getenv("DATABASE_URL")

# Database instance for async usage
database = Database(DATABASE_URL)

# SQLAlchemy metadata object to share across models
metadata = MetaData()

# SQLAlchemy engine for table creation or sync ops
engine = create_engine(DATABASE_URL)
