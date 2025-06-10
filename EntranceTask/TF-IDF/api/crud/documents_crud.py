from api.schemas.documents_schema import DocumentCreate, DocumentRead, DocumentUpdate
from models.document import documents
from api.db import database
from datetime import datetime
from api.utils.logger import logger


# Create
async def create_document(document: DocumentCreate):
    query = documents.insert().values(
        filename=document.filename,
        path=document.path,
        filecontent = document.filecontent,
        user_id=document.user_id,
        uploaded_at=datetime.now()
    )
    try:
        new_id = await database.execute(query)
        return {"id": new_id, **document.dict()}
    except Exception as e:
        print(f"Document creation error: {e}")
        logger.error(f"Document creation error: {e}")
        return None


# Get all for user
async def get_all_documents(user_id: int) -> list[DocumentRead]:
    query = documents.select().where(documents.c.user_id == user_id)
    try:
        rows = await database.fetch_all(query)
        return [DocumentRead(**row) for row in rows]
    except Exception as e:
        print(f"Document fetch all error: {e}")
        logger.error(f"Document fetch all error: {e}")
        return []


# Get by ID
async def get_document_by_id(user_id: int, document_id: int) -> DocumentRead | None:
    query = documents.select().where(
        (documents.c.user_id == user_id) & (documents.c.id == document_id)
    )
    try:
        row = await database.fetch_one(query)
        return DocumentRead(**row) if row else None
    except Exception as e:
        print(f"Document fetch by ID error: {e}")
        logger.error(f"Document fetch by ID error: {e}")
        return None


# Delete
async def delete_document(user_id: int, document_id: int) -> int:
    try:
        doc = await get_document_by_id(user_id, document_id)
        if not doc:
            return 0

        query = documents.delete().where(
            (documents.c.user_id == user_id) & (documents.c.id == document_id)
        )
        await database.execute(query)
        return 1
    except Exception as e:
        print(f"Document delete error: {e}")
        logger.error(f"Document delete error: {e}")
        return 0


# Update
async def update_document(user_id: int, document_id: int, update: DocumentUpdate):
    try:
        existing = await get_document_by_id(user_id, document_id)
        if not existing:
            return None

        update_values = update.dict(exclude_unset=True)
        if not update_values:
            return existing

        query = documents.update().where(
            (documents.c.user_id == user_id) & (documents.c.id == document_id)
        ).values(**update_values)

        await database.execute(query)
        return await get_document_by_id(user_id, document_id)
    except Exception as e:
        print(f"Document update error: {e}")
        logger.error(f"Document update error: {e}")
        return None
