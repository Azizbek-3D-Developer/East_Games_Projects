from fastapi import Request, Depends, status, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from api.utils.router import router
from api.utils.templates import templates
from api.auth.dependencies import get_current_user 
from api.crud.user_crud import update_user as update_user_in_db, delete_user as delete_user_in_db
from api.schemas.user_schema import UserRead, UserUpdate



@router.get("/dashboard", response_class=HTMLResponse)
async def login_to_dashboard(request: Request, user = Depends(get_current_user)):
    return templates.TemplateResponse("Dashboard/dashboard.html", {
        "request": request,
        "user_email": user.email  # Use user.email here
    })
   
   
    
@router.get("/logout")
async def logout_user():
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("access_token")
    return response



@router.get("/setting", response_class=HTMLResponse)
async def user_settings_page(request: Request, user=Depends(get_current_user)):
    return templates.TemplateResponse("Dashboard/settings-page.html", {
        "request": request,
        "user": user
    })



@router.post("/setting", response_class=HTMLResponse)
async def setting_post(
    request: Request,
    email: str = Form(None),
    username: str = Form(None),
    password: str = Form(None),
    current_user=Depends(get_current_user)
):
    user_id = current_user["id"]

    update_data = {}
    if email:
        update_data["email"] = email
    if username:
        update_data["username"] = username
    if password:
        update_data["password"] = password

    if not update_data:
        # Nothing to update, just reload page or return some message
        response = RedirectResponse(url="/setting", status_code=303)
        return response

    updated_user = await update_user_in_db(user_id, update_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or update failed")

    # Redirect back to settings page after successful update
    response = RedirectResponse(url="/dashboard?update=success", status_code=303)
    return response



@router.put("/{user_id}", response_model=UserRead)
async def update_user_page(user_id: int, user_update: UserUpdate, current_user=Depends(get_current_user)):
    if current_user["id"] != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this user")

    updated_user = await update_user_in_db(user_id, user_update.dict(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or update failed")
    return updated_user

@router.post("/setting/{user_id}/delete")
async def delete_user_post(
    user_id: int,
    current_user=Depends(get_current_user)
):
    if current_user["id"] != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this user")

    deleted_user = await delete_user_in_db(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found or delete failed")

    response = RedirectResponse(url="/?delete_status=success", status_code=303)
    response.delete_cookie("access_token")  
    return response
