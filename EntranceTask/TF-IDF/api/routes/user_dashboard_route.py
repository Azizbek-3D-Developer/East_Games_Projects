from fastapi import Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from api.utils.router import router
from api.utils.templates import templates
from api.auth.dependencies import get_current_user 

@router.get("/dashboard", response_class=HTMLResponse)
async def login_to_dashboard(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse("Dashboard/dashboard.html", {
        "request": request,
        "user_email": user  
    })
    
@router.get("/logout")
async def logout_user():
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("access_token")
    return response