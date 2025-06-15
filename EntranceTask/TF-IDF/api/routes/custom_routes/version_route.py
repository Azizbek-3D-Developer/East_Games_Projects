from fastapi import Request
from fastapi.responses import HTMLResponse
from api.utils.templates import templates
from api.utils.router import router
import os
from api.utils.dotenv_load import env_loader
# print("Loaded APP_VERSION from .env:", os.getenv("APP_VERSION")) # successfull result

APP_VERSION = os.getenv("APP_VERSION", "3.0.0")

@router.get("/version", response_class=HTMLResponse, tags=["Version"])
async def status_page(request: Request):
    print(f"version: {APP_VERSION}") 
    return templates.TemplateResponse(
        "LandingPage/version-page.html", 
        {"app_version": APP_VERSION,
        "request": request}
        )