from api.utils.router import router
from api.utils.templates import templates
from fastapi import Request, Depends, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from typing import List
from api.auth.dependencies import get_current_user
from api.crud.collection_document_crud import (
    get_collection_document,
    get_collections_by_document,
    get_documents_by_collection,
    create_collection_document_link,
    delete_collection_document_link
)

# For page Collections / Details
@router.post(f"/collections/details/{{collection_id}}/create", tags=["Collections-Documents"])
async def create_collection_document_link_request(
    collection_id: int,
    document_ids: List[int] = Form(...),
    user=Depends(get_current_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated")

    for doc_id in document_ids:
        # checking if such connection exists
        existing = await get_collection_document(collection_id, doc_id)
        if existing:
            continue  # Skip already linked documents

        result = await create_collection_document_link(collection_id, doc_id)
        if not result == 1:
            print("error")
            # raise HTTPException(status_code=400, detail="Could not create collection-document connection")

    return RedirectResponse(
        url=f"/dashboard/collections/{collection_id}",
        status_code=status.HTTP_303_SEE_OTHER
    )


# For page document details
@router.post(f"/documents/details/{{document_id}}/create",  tags=["Collections-Documents"])
async def create_document_collection_link_request(
    document_id: int,
    collections_ids: List[int] = Form(...),
    user=Depends(get_current_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated")

    for col_id in collections_ids:
        # checking if such connection exists
        existing = await get_collection_document(document_id, col_id)
        if existing:
            continue  # Skip already linked documents

        result = await create_collection_document_link(col_id, document_id)
        if not result == 1:
            print("error")
            # raise HTTPException(status_code=400, detail="Could not create collection-document connection")

    return RedirectResponse(
        url=f"/dashboard/documents/{document_id}",
        status_code=status.HTTP_303_SEE_OTHER
    )



# Deleting the connection
@router.post(f"/collections/details/{{collection_id}}/{{document_id}}/delete",  tags=["Collections-Documents"])
async def delete_collection_document_connection(
    collection_id: int,
    document_id: int,
    user=Depends(get_current_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated")

    result = await delete_collection_document_link(collection_id, document_id)
    if result != 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting collection-document link")

    return RedirectResponse(
        url=f"/dashboard/collections/{collection_id}?delete_status=success",
        status_code=status.HTTP_303_SEE_OTHER
    )
