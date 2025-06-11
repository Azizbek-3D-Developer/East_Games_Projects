from fastapi import Request, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated
from api.utils.router import router
from api.utils.templates import templates
from api.schemas.collection_schema import CreateCollection, CollectionRead, UpdateCollection
from api.utils.links import baselink, col_link
from api.auth.dependencies import get_current_user
from api.crud.collection_crud import get_all_collection, create_new_collection, get_collection_by_id, delete_collection_by_id, update_collection_by_id
from api.crud.documents_crud import get_document_by_id, get_all_documents
from api.crud.collection_document_crud import get_documents_by_collection
from api.services.tf_idf_service import compute_tfidf_from_text_for_statistics, compute_tfidf_from_text


# Get All
@router.get(f"{baselink}{col_link}", response_class=HTMLResponse)
async def list_collections(
    request: Request,
    user = Depends(get_current_user),
):

    colllections_list = await get_all_collection( user.id)
    
    return templates.TemplateResponse(
        "Dashboard/Collections/collection.html",
        {
            "request": request,
            "user_email": user.email,
            "collections": colllections_list,
        },
    )
    
    
# Create route    
@router.get(f"{baselink}{col_link}/create", response_class=HTMLResponse)
async def get_create_page(
    request: Request,
    user = Depends(get_current_user),
):

    return templates.TemplateResponse(
        "Dashboard/Collections/collection-create.html",
        {
            "request": request,
            "user_email": user.email,
        },
    )
    
  
    
@router.post(f"{baselink}{col_link}/create")
async def create_new_collection_page(
    request: Request,
    name: str = Form(..., min_length=5, max_length=50),
    user=Depends(get_current_user),
):
    user_id = user.id
    collection_create = CreateCollection(name=name, user_id=user_id)
    created_collection = await create_new_collection(collection_create)
    
    if not created_collection:
        raise HTTPException(status_code=400, detail="Collection creation failed")

    return RedirectResponse(
        url=f"{baselink}{col_link}/{created_collection['id']}",
        status_code=status.HTTP_303_SEE_OTHER
    )
  
    
# details
@router.get(f"{baselink}{col_link}/{{collection_id}}", response_class=HTMLResponse)
async def get_details_page(
    request: Request,
    collection_id: int,
    user = Depends(get_current_user),
):
    user_id = user.id
    collection_item = await get_collection_by_id(user_id, collection_id)
    if not collection_item:
        raise HTTPException(status_code=400, detail="Collection item not found")
    
    related_documents_ids = await get_documents_by_collection(collection_item.id)
    
    collection_documents = []
    for doc_id in related_documents_ids:
        doc = await get_document_by_id(user.id, doc_id.document_id)

        if doc:
            collection_documents.append(doc)
    
    documents_list = await get_all_documents(user.id)
    if not documents_list:
        documents_list = []
        
    if not collection_item:
        raise HTTPException(status_code=400, detail="Collection finding failed")
    return templates.TemplateResponse(
        "Dashboard/Collections/collection-details.html",
        {
            "request": request,
            "user_email": user.email,
            "collection_item": collection_item,
            "owner_name": user.username,
            "collection_id" : collection_item.id,
            "documents": collection_documents,
            "all_documents": documents_list
        },
    )
 
 
 
# Delete
@router.post(f"{baselink}{col_link}/{{collection_id}}/delete")
async def delete_the_collection_page(
    request: Request,
    collection_id: int,
    user=Depends(get_current_user),
):
    user_id = user.id
    
    result = await delete_collection_by_id(user_id=user_id, collection_id=collection_id)
    
    if result == 1:
        return RedirectResponse(url=f"{baselink}{col_link}", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return templates.TemplateResponse(
            "Dashboard/Collections/collection.html",
            {
                "request": request,
                "message": "Failed to delete collection or collection not found.",
            },
            status_code=400,
        )
        
        
# Update
@router.get(f"{baselink}{col_link}/{{collection_id}}/edit")
async def get_update_page(
    request:Request,
    collection_id: int,
    user=Depends(get_current_user),
    
    ):
    user_id = user.id
    collection_item = await get_collection_by_id(user_id, collection_id)
    
    if not collection_item:
        raise HTTPException(status_code=400, detail="Collection finding failed")
    
    return templates.TemplateResponse(
        "Dashboard/Collections/collection-update.html",
        {
            "request": request,
            "user_email": user.email,
            "collection" : collection_item
        },
        )
    
    
    
@router.post(f"{baselink}{col_link}/{{collection_id}}/edit")
async def create_new_collection_page(
    request: Request,
    collection_id: int,
    name: str = Form(..., min_length=5, max_length=50),
    user=Depends(get_current_user),
):
    user_id = user.id
    collectionUpdate = UpdateCollection(name=name)
    updated_collection = await update_collection_by_id(user_id, collection_id, collectionUpdate)
    
    if not updated_collection:
        raise HTTPException(status_code=400, detail="Collection creation failed")

    return RedirectResponse(
        url=f"{baselink}{col_link}/{updated_collection.id}",
        status_code=status.HTTP_303_SEE_OTHER
    )
  
  
 
 
# Statistics for collections  
@router.get(f"{baselink}{col_link}/{{collection_id}}/statistics", response_class=HTMLResponse)
async def get_statistics_for_collection_documents_page(
    request: Request,
    collection_id: int,
    user = Depends(get_current_user)
):
    # Get doc IDs from the junction table
    collection_documents_list_ids = await get_documents_by_collection(collection_id)
    
    # print("Fetched doc IDs from junction table:", collection_documents_list_ids)

    collection_documents = []
    combined_full_text = ""

    for doc_id in collection_documents_list_ids:
        # print("Getting document with ID:", doc_id.document_id)
        doc = await get_document_by_id(user.id, doc_id.document_id)
        if doc:
            # print(doc.filecontent)
            combined_full_text += f"{doc.filecontent} "
            collection_documents.append(doc)
            # print("document loaded")
        
    text_stats = []
    combined_full_text = combined_full_text.strip(" ")
    if combined_full_text:
        try:
            text_stats = await compute_tfidf_from_text(combined_full_text)
            print(f"result of tf-idf:  {text_stats}")
        except ValueError:
            text_stats = []

    return templates.TemplateResponse(
        "Dashboard/Collections/collection-statistics.html",
        {
            "request": request,
            "useremail": user.email,
            "filetext": combined_full_text,
            "documents": collection_documents,
            "statistics": text_stats,
            "collection_id": collection_id
        }
    )
