from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
from api.utils.templates import templates
from api.utils.router import router



@router.get(
    "/status",
    tags=["Status"],
    responses={
        200: {
            "description": "Returns status in JSON or HTML depending on Accept header",
            "content": {
                "application/json": {
                    "example": {"status": "ok"}
                },
                "text/html": {
                    "example": "<html><body>Status OK</body></html>"
                }
            },
        }
    }
)
async def status_page(request: Request):
    accept = request.headers.get("accept", "")
    if "application/json" in accept:
        return JSONResponse(content={"status": "ok"})
    return templates.TemplateResponse("LandingPage/status-page.html", {"request": request})