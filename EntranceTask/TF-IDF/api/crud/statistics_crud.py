from typing import List, Optional
from sqlalchemy import select, update, delete
from api.db import database
from models.statistics import statistics
from api.schemas.statistics_schema import StatisticsCreate, StatisticsRead, StatisticsUpdate
from datetime import datetime
from api.utils.logger import logger

# Get all statistics by a list of document_ids
async def get_statistics_by_document_ids(document_ids: List[int]) -> List[StatisticsRead]:
    try:
        query = select(statistics).where(statistics.c.document_id.in_(document_ids))
        rows = await database.fetch_all(query)
        return [StatisticsRead(**row) for row in rows]
    except Exception as e:
        print(f"Error in get all statistics: {e}")
        logger.error(f"Error in get all statistics: {e}")
        return []
        


# Get a single statistic by document_id
async def get_statistics_by_document_id(document_id: int) -> Optional[StatisticsRead]:

    try:
        query = select(statistics).where(statistics.c.document_id == document_id)
        row = await database.fetch_one(query)
        return StatisticsRead(**row) if row else None
    except Exception as e:
        print(f"Error in get all statistics: {e}")
        logger.error(f"Error in get by id statistics: {e}")
        return None

# Create a new statistics row
async def create_statistics(stat: StatisticsCreate) -> StatisticsRead:
    
    try:
        query = statistics.insert().values(
            document_id=stat.document_id,
            tfidf_json=stat.tfidf_json,
            created_at=datetime.now()
        )
        result = await database.execute(query)
        return result
    except Exception as e:
        print(f"Error in get all statistics: {e}")
        logger.error(f"Error in create statistics: {e}")
        return None

# Update statistics by document_id
async def update_statistics(document_id: int, stat_update: StatisticsUpdate) -> Optional[StatisticsRead]:
    
    try:
        query = update(statistics).where(statistics.c.document_id == document_id).values(
            tfidf_json=stat_update.tfidf_json
        )
        await database.execute(query)
        return await get_statistics_by_document_id(document_id)
    except Exception as e:
        print(f"Error in get all statistics: {e}")
        logger.error(f"Error in update statistics: {e}")
        return None

# Delete statistics by document_id
async def delete_statistics(document_id: int) -> bool:
    
    try:
        query = delete(statistics).where(statistics.c.document_id == document_id)
        result = await database.execute(query)
        return bool(result)
    except Exception as e:
        print(f"Error in get all statistics: {e}")
        logger.error(f"Error in delete statistics: {e}")
        return []