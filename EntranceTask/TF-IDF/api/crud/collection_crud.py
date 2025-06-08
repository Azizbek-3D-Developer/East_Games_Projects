from api.schemas.collection_schema import CreateCollection, CollectionRead, UpdateCollection
from models.collection import collections
from api.db import database
from datetime import datetime

# Create
async def create_new_collection(collection : CreateCollection):
    query = collections.insert().values(name=collection.name, user_id=collection.user_id, created_at=datetime.now())
    
    try:
        last_record_id = await database.execute(query)
        return {"id": last_record_id, "name": collection.name, "user_id": collection.user_id}
    except Exception as e:
        print(f"Collection creation error: {e}")
        return None


# Get All
async def get_all_collection(user_id:int) -> list[CollectionRead]:
    query = collections.select().where(collections.c.user_id == user_id) 
    try:
        result = await database.fetch_all(query)
        list_of_collections = [CollectionRead(**row) for row in result]
        return list_of_collections
    except Exception as e:
        print(f"Collection Get all error: {e}")
        return []

# Get by id
async def get_collection_by_id(user_id:int, collection_id: int) -> CollectionRead | None:
    query = collections.select().where(
        (collections.c.user_id == user_id) & (collections.c.id == collection_id)
    )
    try:
        
        result = await database.fetch_one(query)
        if result:
              return CollectionRead(**result) 
        return None
    except Exception as e:
        print(f"Collection get by id error: {e}")
        return None


# Delete
async def delete_collection_by_id(user_id:int, collection_id: int) -> int:
    collection_item = await get_collection_by_id(user_id=user_id, collection_id=collection_id)

    try:
        if collection_item:
            query = collections.delete().where(
                (collections.c.user_id == user_id) & (collections.c.id == collection_id)
            )
            await database.execute(query)
            return 1
        else:
            return 0
    except Exception as e:
        print(f"Collection delete error: {e}")
        return 0
    


# Update
async def update_collection_by_id(user_id:int, collection_id: int, new_name: UpdateCollection ):
    try:
        existing = await get_collection_by_id(user_id=user_id, collection_id=collection_id)
        if not existing:
            return None

        update_values = new_name.dict(exclude_unset=True)

        if not update_values:
            return existing  

        query = collections.update().where(
            (collections.c.user_id == user_id) & (collections.c.id == collection_id)
        ).values(**update_values)

        await database.execute(query)

        updated = await get_collection_by_id(user_id, collection_id)
        return updated

    except Exception as e:
        print(f"Collection update error: {e}")
        return None