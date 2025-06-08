from fastapi import Request
from fastapi.responses import HTMLResponse
from api.utils.templates import templates
from api.utils.router import router


@router.get("/status", response_class=HTMLResponse)
async def status_page(request: Request):
    print("status: OK") 
    return templates.TemplateResponse("LandingPage/status-page.html", {"request": request})