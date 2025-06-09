from fastapi import UploadFile, File, Request, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from api.utils.router import router
from api.utils.templates import templates
from api.utils.links import baselink
from api.auth.dependencies import get_current_user
from api.crud.documents_crud import create_document, get_all_documents, get_document_by_id, delete_document
from api.crud.statistics_crud import create_statistics, get_statistics_by_document_id, get_latest_statistics_by_document_id
from api.services.tf_idf_service import compute_tfidf_from_text
from api.utils.links import doclink, baselink, UPLOAD_DIR
from api.schemas.documents_schema import DocumentCreate
from api.schemas.statistics_schema import StatisticsCreate
import os
from api.db import database, metrics_service
import time
import shutil

@router.on_event("startup")
async def startup():
    await database.connect()

@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()

UPLOAD_FOLDER = UPLOAD_DIR


@router.get(f"{baselink}{doclink}", response_class=HTMLResponse)
async def list_documents(request: Request, user=Depends(get_current_user)):
    documents = await get_all_documents(user.id)
    return templates.TemplateResponse(
        "Dashboard/documents/document.html",
        {"request": request, "user_email": user.email, "documents": documents},
    )


@router.get(f"{baselink}{doclink}/create", response_class=HTMLResponse, name="document_create_form")
async def get_upload_page(request: Request, user=Depends(get_current_user)):
    return templates.TemplateResponse(
        "Dashboard/documents/document-create.html",
        {"request": request, "user_email": user.email},
    )


@router.post(f"{baselink}{doclink}/create", name="document_create")
async def upload_document(
    request: Request,
    file: UploadFile = File(...),
    user=Depends(get_current_user),
):
    start_time = time.time()
    try:
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)

        text = content.decode("utf-8")
        tfidf_result = await compute_tfidf_from_text(text)

        processing_duration = round(time.time() - start_time, 3)
          
        document_data = DocumentCreate(
            filename=file.filename,
            path=file_location,
            user_id=user.id
        )
        doc_data = await create_document(document_data)

        statistics_data = StatisticsCreate(
            document_id=doc_data["id"],
            tfidf_json=tfidf_result
        )
        await create_statistics(statistics_data)

        await metrics_service.update_metrics(
            processing_duration=processing_duration,
            upload_size_bytes=len(content),
            uploaded_filename=file.filename
        )
        
        return RedirectResponse(
            url=f"{baselink}{doclink}/{doc_data['id']}",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")


@router.get(f"{baselink}{doclink}/{{document_id}}", response_class=HTMLResponse, name="document_detail")
async def document_details(
    request: Request,
    document_id: int,
    user=Depends(get_current_user),
):
    document = await get_document_by_id(user.id, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    statistics = await get_latest_statistics_by_document_id(document_id)

    return templates.TemplateResponse(
        "Dashboard/documents/document-details.html",
        {
            "request": request,
            "user_email": user.email,
            "document": document,
            "statistics": statistics,
        },
    )


# Optional: Add document edit page route
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
        "Dashboard/documents/document-edit.html",
        {
            "request": request,
            "user_email": user.email,
            "document": document,
        },
    )


# Delete document
@router.post(f"{baselink}{doclink}/{{document_id}}/delete", name="document_delete")
async def delete_document_route(
    request: Request,
    document_id: int,
    user=Depends(get_current_user),
):
    result = await delete_document(user.id, document_id)

    if result == 1:
        return RedirectResponse(
            url=f"{baselink}{doclink}", status_code=status.HTTP_303_SEE_OTHER
        )
    else:
        raise HTTPException(status_code=400, detail="Delete failed or not authorized")
