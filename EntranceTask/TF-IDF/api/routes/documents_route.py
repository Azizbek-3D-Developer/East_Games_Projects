from fastapi import UploadFile, File, Request, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from api.utils.router import router
from typing import Optional
from api.utils.templates import templates
from api.utils.logger import logger
from api.utils.links import baselink
from api.auth.dependencies import get_current_user
from api.crud.documents_crud import (
    create_document, get_all_documents, get_document_by_id,
    delete_document, update_document
)
from api.crud.statistics_crud import (
    get_statistics_by_document_ids, get_statistics_by_document_id, create_statistics,
    update_statistics, delete_statistics
)
from api.services.huffman_service import compute_huffman_from_text
from api.crud.huffman_crud import (
    create_huffman_encoding,
    update_huffman_encoding
)
from api.schemas.huffman_schema import (
    HuffmanCreate, 
    HuffmanRead,
    HuffmanUpdate
)
from api.services.tf_idf_service import compute_tfidf_from_text
from api.utils.links import doclink, baselink, UPLOAD_DIR
from api.schemas.documents_schema import DocumentCreate
from api.schemas.statistics_schema import StatisticsCreate, StatisticsUpdate
import os
from api.db import database, metrics_service
import time
import shutil
import uuid
import aiofiles
from api.crud.collection_document_crud import (
    get_collections_by_document, get_collection_document
)
from api.crud.collection_crud import (
    get_collection_by_id, get_all_collection
)

UPLOAD_FOLDER = UPLOAD_DIR

# Documents get all page
@router.get(f"{baselink}{doclink}", response_class=HTMLResponse)
async def list_documents(request: Request, user=Depends(get_current_user)):
    documents = await get_all_documents(user.id)
    return templates.TemplateResponse(
        "Dashboard/documents/document.html",
        {"request": request, "user_email": user.email, "documents": documents},
    )


# Documents Create page loading
@router.get(f"{baselink}{doclink}/create", response_class=HTMLResponse, name="document_create_form")
async def get_upload_page(request: Request, user=Depends(get_current_user)):
    return templates.TemplateResponse(
        "Dashboard/documents/document-create.html",
        {"request": request, "user_email": user.email},
    )


# Documents create logic handling
@router.post(f"{baselink}{doclink}/create", name="document_create")
async def upload_document(
    request: Request,
    file: UploadFile = File(...),
    filename: str = Form(...),
    user=Depends(get_current_user),
):
    start_time = time.time()
    try:
        user_folder = os.path.join(UPLOAD_FOLDER, str(user.id))
        os.makedirs(user_folder, exist_ok=True)

        safe_filename = os.path.basename(file.filename)
        unique_filename = f"a-a_{safe_filename}"
        file_location = os.path.join(user_folder, unique_filename)

        if filename == "":
            filename = unique_filename
        
        # Async file save
        async with aiofiles.open(file_location, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)

        # tf-idf 
        text = content.decode("utf-8")
        tfidf_result = await compute_tfidf_from_text(text)

        processing_duration = round(time.time() - start_time, 3)


        # creating new document
        document_data = DocumentCreate(
            filename=filename,
            path=os.path.join(str(user.id), unique_filename),  # relative path
            user_id=user.id,
            filecontent=text
        )
        
        doc_data = await create_document(document_data) # getting the id of the created document

        
        # creating the statistics for the document
        statistics_data = StatisticsCreate(
            document_id=doc_data["id"],
            tfidf_json=tfidf_result
        )
        await create_statistics(statistics_data)
        # ➕ Create Huffman data
        try:
            text = text.strip()
            huffman_result = await compute_huffman_from_text(text)

            cleaned_huffman = [
                pair for pair in huffman_result
                if pair.get("letter") and pair.get("code")
            ]

            huffman_data = HuffmanCreate(
                document_id=doc_data["id"],
                user_id=user.id,
                pairs=cleaned_huffman
            )
            await create_huffman_encoding(huffman_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Huffman generation failed: {e}")


        # updating the metrics for the document
        await metrics_service.update_metrics(
            processing_duration=processing_duration,
            upload_size_bytes=len(content),
            uploaded_filename=unique_filename
        )

        return RedirectResponse(
            url=f"{baselink}{doclink}/{doc_data['id']}",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")


# details page
@router.get(f"{baselink}{doclink}/{{document_id}}", response_class=HTMLResponse, name="document_detail")
async def document_details(
    request: Request,
    document_id: int,
    user=Depends(get_current_user),
):
    # Get the document
    document = await get_document_by_id(user.id, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    # Getting related collections id for this document
    document_collections_ids = await get_collections_by_document(document_id)
    
    # assigning collections into list
    collections_list = []
    for col_id in document_collections_ids:
        # getting each collection item from db
        collection_item = await get_collection_by_id(user.id, col_id.collection_id)

        # adding into final list
        if collection_item:
            collections_list.append(collection_item)
    
    # Getting the list of all collections for this user
    all_collections = await get_all_collection(user.id)
    if not all_collections:
        # raise HTTPException(status_code=400, detail= "Could not get all collections for documents")
        all_collections = []
    
    
    # Get the latest statistics object (includes ID and tfidf)
    stat_obj = await get_statistics_by_document_id(document_id)
    if not stat_obj:
        raise HTTPException(status_code=404, detail="Statistics not found")

    return templates.TemplateResponse(
        "Dashboard/documents/document-details.html",
        {
            "request": request,
            "user_email": user.email,
            "document": document,
            "statistics": stat_obj,
            "collections": collections_list,
            "all_collections": all_collections
        },
    )



# update page load
@router.get(f"{baselink}{doclink}/{{document_id}}/edit", response_class=HTMLResponse, name="document_edit")
async def document_edit_page(
    request: Request,
    document_id: int,
    user=Depends(get_current_user),
):
    document = await get_document_by_id(user.id, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return templates.TemplateResponse(
        "Dashboard/documents/document-update.html",
        {
            "request": request,
            "user_email": user.email,
            "document": document,
        },
    )


# updating the new document
@router.post(f"{baselink}{doclink}/{{document_id}}/edit", name="document_update")
async def update_document_route(
    request: Request,
    document_id: int,
    filename: str = Form(...),
    file: Optional[UploadFile] = File(None),
    user=Depends(get_current_user),
):
    existing_doc = await get_document_by_id(user.id, document_id)
    if not existing_doc:
        raise HTTPException(status_code=404, detail="Document not found")

    new_filename = filename.strip()
    update_data = None

    if file:
        start_time = time.time()

        # Set up upload folder
        user_folder = os.path.join(UPLOAD_DIR, str(user.id))
        os.makedirs(user_folder, exist_ok=True)

        # Delete the old file if it exists
        old_file_path = os.path.join(UPLOAD_DIR, existing_doc.path)
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

        # Save new file
        safe_filename = os.path.basename(file.filename)
        if not safe_filename.startswith("a-a_"):
            safe_filename = f"a-a_{safe_filename}"
        new_file_path = os.path.join(user_folder, safe_filename)

        async with aiofiles.open(new_file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)

        relative_path = os.path.join(str(user.id), safe_filename)

        # Prepare update for documents table
        

        # Recompute TF-IDF
        text = content.decode("utf-8")
        tfidf_result = await compute_tfidf_from_text(text)
        
        from api.schemas.documents_schema import DocumentUpdate
        update_data = DocumentUpdate(
            filename=new_filename or safe_filename,
            path=relative_path,
            filecontent = text
        )

        # Update statistics
        from api.schemas.statistics_schema import StatisticsUpdate
        stat_record = await get_statistics_by_document_id(document_id)
        if not stat_record:
            raise HTTPException(status_code=404, detail="Statistics not found")

        statistics_data = StatisticsUpdate(tfidf_json=tfidf_result)
        await update_statistics(document_id, statistics_data)

        text = text.strip()
        # Recompute Huffman encoding
        huffman_result = await compute_huffman_from_text(text)

        # Clean invalid Huffman pairs (e.g. empty letter or code)
        cleaned_pairs = [
            pair for pair in huffman_result
            if pair.get("letter") and pair.get("code")
        ]

        # Update Huffman encoding in DB
        huffman_update_data = HuffmanUpdate(
            user_id=user.id,
            document_id=document_id,
            pairs=cleaned_pairs
        )
        await update_huffman_encoding(huffman_update_data)

        
        # Log updated metrics
        processing_duration = round(time.time() - start_time, 3)
        await metrics_service.update_metrics(
            processing_duration=processing_duration,
            upload_size_bytes=len(content),
            uploaded_filename=safe_filename
        )
    else:
        from api.schemas.documents_schema import DocumentUpdate
        update_data = DocumentUpdate(
            filename=new_filename or existing_doc.filename,
            path=existing_doc.path,
            filecontent= existing_doc.filecontent            
        )

    updated_doc = await update_document(user.id, document_id, update_data)
    if not updated_doc:
        raise HTTPException(status_code=400, detail="Document update failed")

    return RedirectResponse(
        url=f"{baselink}{doclink}/{document_id}",
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.post(f"{baselink}{doclink}/{{document_id}}/delete", name="document_delete")
async def delete_document_route(
    request: Request,
    document_id: int,
    user=Depends(get_current_user),
):
    # Get the document first (before deleting it from DB)
    doc = await get_document_by_id(user.id, document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    # Try to delete from database
    result = await delete_document(user.id, document_id)
    if result == 1:
        # Delete statistics
        await delete_statistics(document_id)

        # Delete file from folder
        full_path = os.path.join(UPLOAD_DIR, doc.path)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            try:
                os.remove(full_path)
                logger.info(f"Deleted file from disk: {full_path}")
            except Exception as e:
                logger.error(f"Failed to delete file from disk: {e}")
        else:
            logger.warning(f"File does not exist or is not a file: {full_path}")

        return RedirectResponse(
            url=f"{baselink}{doclink}", status_code=status.HTTP_303_SEE_OTHER
        )

    else:
        raise HTTPException(status_code=400, detail="Delete failed or not authorized")
