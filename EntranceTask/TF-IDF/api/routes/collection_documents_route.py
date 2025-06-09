# @router.post("/create-connection")
# async def create_connection(
#     source_type: str = Form(...),  # 'document' or 'collection'
#     source_id: int = Form(...),
#     target_ids: list[int] = Form(...),  # multiple selected ids
#     user = Depends(get_current_user),
# ):
#     # Validate source ownership
#     if source_type == "document":
#         # check document belongs to user
#         # insert collection_documents rows for each collection id in target_ids
#         await create_links_for_document(source_id, target_ids, user.id)
#     elif source_type == "collection":
#         # check collection belongs to user
#         # insert collection_documents rows for each document id in target_ids
#         await create_links_for_collection(source_id, target_ids, user.id)
#     else:
#         raise HTTPException(400, "Invalid source type")

#     # redirect or return success message
#     return RedirectResponse(f"/{source_type}s/{source_id}", status_code=303)



