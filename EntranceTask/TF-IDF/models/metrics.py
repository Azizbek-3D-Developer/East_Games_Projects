from datetime import datetime
from sqlalchemy import Table, Column, Integer, Float, DateTime, MetaData
from databases import Database
from .user import metadata

metrics = Table(
    "metrics",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("files_processed", Integer, default=0),
    Column("min_time_processed", Float),
    Column("avg_time_processed", Float),
    Column("max_time_processed", Float),
    Column("latest_file_processed_timestamp", DateTime),
)