from models.collection_document import collection_documents
from api.db import database
from api.schemas.collection_documents_schema import  CollectionDocumentRead
from typing import Optional, List
from api.utils.logger import logger


# Create a new link between collection and document
async def create_collection_document_link(col_id: int, document_id:int ) -> int:
    query = collection_documents.insert().values(
        collection_id=col_id,
        document_id=document_id
    )
    try:
        result = await database.execute(query)
        return 1 if result else 0
    except Exception as e:
        print(f"CollectionDocument create error: {e}")
        return 0





# Get a specific collection-document link
async def get_collection_document(collection_id: int, document_id: int) -> Optional[CollectionDocumentRead]:
    query = collection_documents.select().where(
        (collection_documents.c.collection_id == collection_id)
        & (collection_documents.c.document_id == document_id)
    )
    try:
        result = await database.fetch_one(query)
        return CollectionDocumentRead(**result) if result else None
    except Exception as e:
        logger.error(f"Collection Document error in get by id: {e}")
        return None


# Get all document links for a given collection
async def get_documents_by_collection(collection_id: int) -> List[CollectionDocumentRead]:
    query = collection_documents.select().where(collection_documents.c.collection_id == collection_id)
    try:
        rows = await database.fetch_all(query)
        return [CollectionDocumentRead(**row) for row in rows] if rows else []
    except Exception as e:
        print(f"CollectionDocument fetch by collection error: {e}")
        return []


# Get all collection links for a given document
async def get_collections_by_document(document_id: int) -> List[CollectionDocumentRead]:
    query = collection_documents.select().where(collection_documents.c.document_id == document_id)
    try:
        rows = await database.fetch_all(query)
        return [CollectionDocumentRead(**row) for row in rows] if rows else []
    except Exception as e:
        print(f"CollectionDocument fetch by document error: {e}")
        return []


# Delete a link between collection and document
async def delete_collection_document_link(collection_id: int, document_id: int) -> int:
    query = collection_documents.delete().where(
        (collection_documents.c.collection_id == collection_id) &
        (collection_documents.c.document_id == document_id)
    )
    try:
        result = await database.execute(query)
        return 1 if result else 0
    except Exception as e:
        print(f"CollectionDocument delete error: {e}")
        return 0
