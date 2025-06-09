from datetime import datetime
from databases import Database
from models import metrics


class MetricsService:
    def __init__(self, database: Database):
        self.database = database

    async def update_metrics(self, processing_duration: float, upload_size_bytes: int = 0, uploaded_filename: str = ""):
        """Update the metrics table with new processing time and upload info."""

        now = datetime.utcnow()
        query = metrics.select().limit(1)
        row = await self.database.fetch_one(query)

        if row is None:
            # Insert first record
            await self.database.execute(
                metrics.insert().values(
                    files_processed=1,
                    min_time_processed=processing_duration,
                    avg_time_processed=processing_duration,
                    max_time_processed=processing_duration,
                    latest_file_processed_timestamp=now,
                    total_upload_size_bytes=upload_size_bytes,
                    last_uploaded_filename=uploaded_filename
                )
            )
        else:
            # Update existing record
            new_files_processed = row["files_processed"] + 1
            new_min = min(row["min_time_processed"], processing_duration)
            new_max = max(row["max_time_processed"], processing_duration)
            new_avg = round(
                ((row["avg_time_processed"] * row["files_processed"]) + processing_duration)
                / new_files_processed, 3
            )
            new_total_size = (row["total_upload_size_bytes"] or 0) + upload_size_bytes
            new_last_filename = uploaded_filename or row["last_uploaded_filename"]

            await self.database.execute(
                metrics.update().where(metrics.c.id == row["id"]).values(
                    files_processed=new_files_processed,
                    min_time_processed=new_min,
                    avg_time_processed=new_avg,
                    max_time_processed=new_max,
                    latest_file_processed_timestamp=now,
                    total_upload_size_bytes=new_total_size,
                    last_uploaded_filename=new_last_filename
                )
            )

    async def get_metrics(self):
        """Fetch the latest metrics from the database."""

        query = metrics.select().order_by(metrics.c.id.desc()).limit(1)
        row = await self.database.fetch_one(query)

        if row:
            return {
                "files_processed": row["files_processed"],
                "min_time_processed": round(row["min_time_processed"], 3) if row["min_time_processed"] else None,
                "avg_time_processed": round(row["avg_time_processed"], 3) if row["avg_time_processed"] else None,
                "max_time_processed": round(row["max_time_processed"], 3) if row["max_time_processed"] else None,
                "latest_file_processed_timestamp": row["latest_file_processed_timestamp"].timestamp() if row["latest_file_processed_timestamp"] else None,
                "total_upload_size_bytes": row["total_upload_size_bytes"] or 0,
                "last_uploaded_filename": row["last_uploaded_filename"] or ""
            }
        else:
            return {
                "files_processed": 0,
                "min_time_processed": None,
                "avg_time_processed": None,
                "max_time_processed": None,
                "latest_file_processed_timestamp": None,
                "total_upload_size_bytes": 0,
                "last_uploaded_filename": ""
            }
