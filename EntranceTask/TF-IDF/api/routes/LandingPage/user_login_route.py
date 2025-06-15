from fastapi import Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated
from api.utils.router import router
from api.utils.templates import templates
from api.crud.user_crud import get_user_by_useremail
from api.utils.security import verify_password 
from api.auth.jwt_auth import create_access_token



UserEmailType = Annotated[
    str,
    Form(
        ...,
        title="Email",
        description="Your Gmail address used to log in",
        min_length=11,
        max_length=50,
        pattern=r"^[a-zA-Z0-9._%+-]+@gmail\.com$",
        example="user@gmail.com"
    )
]

PasswordType = Annotated[
    str,
    Form(
        ...,
        title="Password",
        description="Your account password, at least 6 characters",
        min_length=6,
        example="strongpassword123"
    )
]


@router.get("/login", response_class=HTMLResponse, tags=["Users"])
async def login_page(request: Request):
    return templates.TemplateResponse("LandingPage/login-page.html", {"request": request})


@router.post("/login", summary="Login user and set JWT cookie", response_description="Redirect to dashboard if login is successful",  tags=["Users"])
async def login_user(request: Request,  email: UserEmailType, password: PasswordType):
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