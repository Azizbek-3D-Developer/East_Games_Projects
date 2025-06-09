from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from api.utils.templates import templates
from api.utils.router import router
from api.auth.dependencies import get_current_user
from api.db import metrics_service


@router.get("/metrics", response_class=HTMLResponse)
async def status_page(request: Request, user=Depends(get_current_user)):
    metrics = await metrics_service.get_metrics()
    return templates.TemplateResponse("Dashboard/metrics.html", {
        "request": request,
        "metrics": metrics
    })
