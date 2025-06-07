from fastapi import Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from api.utils.router import router
from api.utils.templates import templates
from api.crud.user_crud import get_user_by_useremail
from api.utils.security import verify_password 
from api.auth.jwt_auth import create_access_token

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("LandingPage/login-page.html", {"request": request})

# @router.post("/login", summary="Get user from db", response_description="Redirect to dashboard page on success")
# async def login_user(request: Request, email: str = Form(...), password: str = Form(...)):
#     user = await get_user_by_useremail(email)
#     if not user or not verify_password(password, user.password_hash):
#         return templates.TemplateResponse("LandingPage/login-page.html", {
#             "request": request,
#             "error": "Invalid email or password."
#         })

#     return RedirectResponse(url="/dashboard", status_code=303)

@router.post("/login", summary="Login user and set JWT cookie")
async def login_user(request: Request, email: str = Form(...), password: str = Form(...)):
    user = await get_user_by_useremail(email)
    if not user or not verify_password(password, user.password_hash):
        return templates.TemplateResponse("LandingPage/login-page.html", {
            "request": request,
            "error": "Invalid email or password."
        })

    token = create_access_token({"sub": user.email})
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="access_token", value=token, httponly=True, secure=False) 
    return response