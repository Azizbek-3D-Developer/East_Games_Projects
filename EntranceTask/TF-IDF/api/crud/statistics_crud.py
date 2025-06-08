from api.schemas.statistics_schema import StatisticsCreate, StatisticsRead, StatisticsUpdate
from models.statistics import statistics
from api.db import database
from datetime import datetime


# Create
async def create_statistics(stat: StatisticsCreate):
    query = statistics.insert().values(
        document_id=stat.document_id,
        tfidf_json=stat.tfidf_json,
        created_at=datetime.now()
    )
    try:
        new_id = await database.execute(query)
        return {"id": new_id, **stat.dict()}
    except Exception as e:
        print(f"Statistics creation error: {e}")
        return None


# Get all by document_id
async def get_statistics_by_document_id(document_id: int) -> list[StatisticsRead]:
    query = statistics.select().where(statistics.c.document_id == document_id)
    try:
        rows = await database.fetch_all(query)
        return [StatisticsRead(**row) for row in rows]
    except Exception as e:
        print(f"Statistics fetch error: {e}")
        return []


# Get by ID
async def get_statistics_by_id(stat_id: int) -> StatisticsRead | None:
    query = statistics.select().where(statistics.c.id == stat_id)
    try:
        row = await database.fetch_one(query)
        return StatisticsRead(**row) if row else None
    except Exception as e:
        print(f"Statistics fetch by ID error: {e}")
        return None


# Delete
async def delete_statistics(stat_id: int) -> int:
    try:
        stat = await get_statistics_by_id(stat_id)
        if not stat:
            return 0
        query = statistics.delete().where(statistics.c.id == stat_id)
        await database.execute(query)
        return 1
    except Exception as e:
        print(f"Statistics delete error: {e}")
        return 0


# Update
async def update_statistics(stat_id: int, update: StatisticsUpdate):
    try:
        existing = await get_statistics_by_id(stat_id)
        if not existing:
            return None

        update_values = update.dict(exclude_unset=True)
        if not update_values:
            return existing

        query = statistics.update().where(statistics.c.id == stat_id).values(**update_values)
        await database.execute(query)
        return await get_statistics_by_id(stat_id)
    except Exception as e:
        print(f"Statistics update error: {e}")
        return None


async def get_latest_statistics_by_document_id(document_id: int) -> StatisticsRead | None:
    query = (
        statistics.select()
        .where(statistics.c.document_id == document_id)
        .order_by(statistics.c.created_at.desc())
        .limit(1)
    )
    try:
        row = await database.fetch_one(query)
        return StatisticsRead(**row) if row else None
    except Exception as e:
        print(f"Statistics fetch error: {e}")
        return None