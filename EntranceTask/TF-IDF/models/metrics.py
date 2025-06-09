from datetime import datetime
from sqlalchemy import Table, Column, Integer, Float, DateTime, MetaData, String
from databases import Database
from .user import metadata

metrics = Table(
    "metrics",
    metadata,
    Column("id", Integer, primary_key=True, default=1, unique=True),
    Column("files_processed", Integer, default=0),
    Column("min_time_processed", Float),
    Column("avg_time_processed", Float),
    Column("max_time_processed", Float),
    Column("latest_file_processed_timestamp", DateTime),
    Column("total_upload_size_bytes", Integer, default=0),
    Column("last_uploaded_filename", String)    
)


# ## 📊 Metrics  
# Stores aggregated processing metrics for uploaded files, including processing times and custom statistics.

# | Field                        | Type     | Description                                              |
# |------------------------------|----------|----------------------------------------------------------|
# | id                           | Integer  | Primary key, always `1` (singleton row)                   |
# | files_processed              | Integer  | Total number of files processed by the application        |
# | min_time_processed          | Float    | Minimum processing time per file (seconds, 3 decimals)    |
# | avg_time_processed          | Float    | Average processing time per file (seconds, 3 decimals)    |
# | max_time_processed          | Float    | Maximum processing time per file (seconds, 3 decimals)    |
# | latest_file_processed_timestamp | DateTime | Timestamp of the most recent file processing               |
# | total_upload_size_bytes     | Integer  | Sum of sizes (in bytes) of all uploaded files             |
# | last_uploaded_filename      | String   | Filename of the most recently uploaded file               |

# ---