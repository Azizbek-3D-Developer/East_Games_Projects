from fastapi import Request, Form, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from typing import Annotated
from api.utils.templates import templates
from api.utils.router import router
from api.crud.user_crud import get_user_by_username, get_user_by_useremail, create_user
from api.schemas.user_schema import UserCreate


# Validation with Annotated + Form directly
UsernameType = Annotated[
    str,
    Form(..., title="Username", description="Unique username, min length 3, max 30", min_length=3, max_length=30)
]

UserEmailType = Annotated[
    str,
    Form(..., title="Email", description="User email, must be a valid Gmail address", min_length=11, max_length=50, pattern=r"^[a-zA-Z0-9._%+-]+@gmail\.com$")
]

PasswordType = Annotated[
    str,
    Form(..., title="Password", description="Password with min length 6", min_length=6)
]

@router.get("/register", response_class=HTMLResponse,  tags=["Users"])
async def register_page(request: Request):
    return templates.TemplateResponse("LandingPage/register-page.html", {"request": request})



@router.post("/register", summary="Register a new user",  tags=["Users"], response_description="Redirect to landing page on success")
async def register_new_user(
    request: Request,
    username: UsernameType,
    email: UserEmailType, 
    password: PasswordType
):
    existing_user = await get_user_by_username(username)
    if existing_user:
        return templates.TemplateResponse(
            "LandingPage/register-page.html",
            {"request": request, "error": "Username already exists."}
        )

    user_by_email = await get_user_by_useremail(email)
    if user_by_email:
        return templates.TemplateResponse(
            "LandingPage/register-page.html",
            {"request": request, "error": "Email already registered."}
        )

    user_create = UserCreate(username=username, password=password, email=email)
    created_user = await create_user(user_create)
    if not created_user:
        raise HTTPException(status_code=400, detail="User creation failed")

    return RedirectResponse(url="/?register_status=success", status_code=303)
