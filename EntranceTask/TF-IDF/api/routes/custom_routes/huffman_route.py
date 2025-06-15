from fastapi import Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from api.utils.router import router
from api.utils.templates import templates
from api.utils.links import baselink
from api.auth.dependencies import get_current_user
from api.crud.huffman_crud import get_huffman_by_document
from api.crud.documents_crud import get_document_by_id




@router.get(f"{baselink}/documents/{{document_id}}/huffman", response_class=HTMLResponse, tags=["Huffman"])
async def huffman_detail_page(
    request: Request,
    document_id: int,
    user=Depends(get_current_user),
):
    document = await get_document_by_id(user.id, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    huffman_obj = await get_huffman_by_document(user.id, document_id)
    if not huffman_obj:
        raise HTTPException(status_code=404, detail="Huffman encoding not found")

    return templates.TemplateResponse(
        "Dashboard/huffman-detail.html",
        {
            "request": request,
            "user_email": user.email,
            "document": document,
            "huffman": huffman_obj,
        },
    )
