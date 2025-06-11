from api.schemas.huffman_schema import HuffmanCreate, HuffmanRead, HuffmanUpdate
from models.huffman import huffman_encodings
from api.db import database
from datetime import datetime
from typing import List


# ✅ Create Huffman encoding
async def create_huffman_encoding(data: HuffmanCreate) -> dict | None:
    query = huffman_encodings.insert().values(
        user_id=data.user_id,
        document_id=data.document_id,
        pairs=[pair.model_dump() for pair in data.pairs],
        created_at=datetime.now()
    )

    try:
        last_record_id = await database.execute(query)
        return {
            "id": last_record_id,
            "user_id": data.user_id,
            "document_id": data.document_id,
            "pairs": [pair.model_dump() for pair in data.pairs],
        }
    except Exception as e:
        print(f"Huffman creation error: {e}")
        return None


# ✅ Get all encodings for a user
async def get_all_huffman_encodings(user_id: int) -> List[HuffmanRead]:
    query = huffman_encodings.select().where(huffman_encodings.c.user_id == user_id)
    try:
        result = await database.fetch_all(query)
        return [HuffmanRead(**row) for row in result]
    except Exception as e:
        print(f"Huffman get all error: {e}")
        return []


# ✅ Get a Huffman encoding by document ID (user-specific)
async def get_huffman_by_document(user_id: int, document_id: int) -> HuffmanRead | None:
    query = huffman_encodings.select().where(
        (huffman_encodings.c.user_id == user_id) &
        (huffman_encodings.c.document_id == document_id)
    )
    try:
        result = await database.fetch_one(query)
        if result:
            return HuffmanRead(**result)
        return None
    except Exception as e:
        print(f"Huffman get by document error: {e}")
        return None


# ✅ Delete encoding by document ID
async def delete_huffman_by_document(user_id: int, document_id: int) -> int:
    try:
        existing = await get_huffman_by_document(user_id, document_id)
        if not existing:
            return 0

        query = huffman_encodings.delete().where(
            (huffman_encodings.c.user_id == user_id) &
            (huffman_encodings.c.document_id == document_id)
        )
        await database.execute(query)
        return 1
    except Exception as e:
        print(f"Huffman delete error: {e}")
        return 0


# ✅ Update Huffman encoding by document ID
async def update_huffman_encoding(data: HuffmanUpdate) -> dict | None:
    try:
        existing = await get_huffman_by_document(data.user_id, data.document_id)
        if not existing:
            return None  # No existing encoding to update

        query = huffman_encodings.update().where(
            (huffman_encodings.c.user_id == data.user_id) &
            (huffman_encodings.c.document_id == data.document_id)
        ).values(
            pairs=[pair.model_dump() for pair in data.pairs],
            created_at=datetime.now()  # optional: update timestamp
        )

        await database.execute(query)
        return {
            "user_id": data.user_id,
            "document_id": data.document_id,
            "pairs": [pair.model_dump() for pair in data.pairs],
        }

    except Exception as e:
        print(f"Huffman update error: {e}")
        return None