from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MetricsRead(BaseModel):
    files_processed: int
    min_time_processed: Optional[float]
    avg_time_processed: Optional[float]
    max_time_processed: Optional[float]
    latest_file_processed_timestamp: Optional[datetime]
    total_upload_size_bytes: int
    last_uploaded_filename: str

    class Config:
        from_attributes = True

