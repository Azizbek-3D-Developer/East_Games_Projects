from databases import Database
from models import metrics
from typing import Optional

class MetricsCRUD:
    def __init__(self, db: Database):
        self.db = db

    async def get_metrics(self):
        query = metrics.select().limit(1)
        return await self.db.fetch_one(query)

    async def update_metrics(self, **kwargs):
        row = await self.get_metrics()
        if not row:
            # Insert if no record exists
            await self.db.execute(metrics.insert().values(**kwargs))
        else:
            # Update existing record
            await self.db.execute(metrics.update().where(metrics.c.id == row["id"]).values(**kwargs))
