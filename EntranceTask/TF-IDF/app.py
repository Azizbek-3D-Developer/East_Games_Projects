from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from api.utils.templates import templates
from api.db import database
from starlette.exceptions import HTTPException as StarletteHTTPException
import os
from dotenv import load_dotenv
from api.routes import api_router
from api.db import DATABASE_URL
from contextlib import asynccontextmanager
from api.utils.dotenv_load import env_loader


# Read config from environment variables
APP_PORT = int(os.getenv("APP_PORT", 6000))
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
TOP_K_WORDS = int(os.getenv("TOP_K_WORDS", 50))
APP_VERSION = os.getenv("APP_VERSION", "3.0.0")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_db()
    yield
    await database.disconnect()


# Main Logic 
app = FastAPI()

# Static items folder root
app.mount("/static", StaticFiles(directory="static"), name="static")

# routes
app.include_router(api_router)

# custom error 404 page
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code >= 400 and exc.status_code <= 499:
        return templates.TemplateResponse("error-404.html", {"request": request,  "error": exc.detail}, status_code=404)
    return await app.default_exception_handler(request, exc)


# custom error 500 page
@app.exception_handler(Exception)
async def internal_exception_handler(request: Request, exc: Exception):
    return templates.TemplateResponse("error-500.html", {"request": request, "error": str(exc)}, status_code=500)


@app.get("/test-500")
async def test_500_error():
    1 / 0


async def connect_to_db():
    await database.connect()
    if "sqlite" in DATABASE_URL:
        await database.execute("PRAGMA foreign_keys = ON;").close()


# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("app:app", host="0.0.0.0", port=APP_PORT, reload=True)
    # uvicorn.run("app:app", host="0.0.0.0", port=7000, reload=True)
    

# http://localhost:8000/