from fastapi import Request
from fastapi.responses import HTMLResponse
from api.utils.templates import templates
from api.utils.router import router


# Render the Landing Page of the Web Service
@router.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    return templates.TemplateResponse("LandingPage/landing-page.html", {"request": request})

