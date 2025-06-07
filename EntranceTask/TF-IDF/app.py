from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from api.utils.templates import templates
from api.db import database
from starlette.exceptions import HTTPException as StarletteHTTPException


# importing the routes
from api.routes.landing_route import router as landing_router


# Main Logic 
app = FastAPI()

# Static items folder root
app.mount("/static", StaticFiles(directory="static"), name="static")

# routes
app.include_router(landing_router) 


# custom error 404 page
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code >= 400 and exc.status_code <= 499:
        return templates.TemplateResponse("error-404.html", {"request": request,  "error": exc.detail}, status_code=404)
    return await app.default_exception_handler(request, exc)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    
    
# http://localhost:8000/