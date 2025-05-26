# Azizbek Axmatjonov
# Project based on task Provided by Nargiza Ruzaeva (Recruiter of Lesta Games) Time: 02.05.2025

# Libraries
from fastapi import FastAPI, Request, UploadFile, File # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
import shutil, os
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore

# env variable
# Task 1 Added
from dotenv import load_dotenv
load_dotenv()

# Metrics
# Task 1 Added
import time
from datetime import datetime

# Database
# Task 3.1 Added
from databases import Database # type: ignore
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, DateTime, select, update
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./metrics.db")

database = Database(DATABASE_URL)
metadata = MetaData()

metrics = Table(
    "metrics",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("files_processed", Integer, default=0),
    Column("min_time_processed", Float),
    Column("avg_time_processed", Float),
    Column("max_time_processed", Float),
    Column("latest_file_processed_timestamp", DateTime),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# Environment variables
APP_PORT = int(os.getenv("APP_PORT", 8000))
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "metrics_db")

# Main Variables Setup
app = FastAPI()

# Static items folder root
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja framework used for rendering HTML files
templates = Jinja2Templates(directory="Templetes")

# Creating upload directory
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads") # Task 1 adjustments
TOP_K_WORDS = int(os.getenv("TOP_K_WORDS", 50)) # Task 1 adjustments

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Default link called
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request}) # Landing page of the Application


@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):

    start_time = time.time()  # Start timing the processing
    
    # Save uploaded file
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read file contents
    with open(file_location, "r", encoding="utf-8") as f:
        text = f.read()

    # Calculate TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([text])
    tfidf_scores = dict(zip(vectorizer.get_feature_names_out(), X.toarray()[0]))
    sorted_words = sorted(tfidf_scores.items(), key=lambda x: -x[1])[:TOP_K_WORDS]

    # Task 1
    processing_duration = round(time.time() - start_time, 3)
    now = datetime.utcnow()

    query = metrics.select().limit(1)
    row = await database.fetch_one(query)

    if row is None:
        # metrics 
        await database.execute(
            metrics.insert().values(
                files_processed=1,
                min_time_processed=processing_duration,
                avg_time_processed=processing_duration,
                max_time_processed=processing_duration,
                latest_file_processed_timestamp=now
            )
        )
    else:
        # metrics
        new_files_processed = row["files_processed"] + 1
        new_min = min(row["min_time_processed"], processing_duration)
        new_max = max(row["max_time_processed"], processing_duration)
        new_avg = round(
            ((row["avg_time_processed"] * row["files_processed"]) + processing_duration)
            / new_files_processed, 3
        )

        await database.execute(
            metrics.update().where(metrics.c.id == row["id"]).values(
                files_processed=new_files_processed,
                min_time_processed=new_min,
                avg_time_processed=new_avg,
                max_time_processed=new_max,
                latest_file_processed_timestamp=now
            )
        )

    # Render results page
    return templates.TemplateResponse("results.html", {
        "request": request,
        "results": sorted_words
    })
    

# Route local-server/status 
# Task 1 Added
@app.get("/status")
async def get_status():
    return {"status": "OK"}


# Route local-server/version
# Task 1 Added
@app.get("/version")
async def get_version():
    return {"version": APP_VERSION}


# Route local-server/metrics
# Task 1 added
@app.get("/metrics")
async def get_metrics():
    query = metrics.select().order_by(metrics.c.id.desc()).limit(1)
    result = await database.fetch_one(query)

    if result:
        return {
            "files_processed": result["files_processed"],
            "min_time_processed": round(result["min_time_processed"], 3),
            "avg_time_processed": round(result["avg_time_processed"], 3),
            "max_time_processed": round(result["max_time_processed"], 3),
            "latest_file_processed_timestamp": result["latest_file_processed_timestamp"].timestamp()
        }
    else:
        return {
            "files_processed": 0,
            "min_time_processed": None,
            "avg_time_processed": None,
            "max_time_processed": None,
            "latest_file_processed_timestamp": None
        }


# Startup and shutdown events
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# runing code
# pip install -r requirements.txt
# uvicorn main:app --reload # old command to run
# uvicorn main:app --host 0.0.0.0 --port $APP_PORT --reload # new command causes error
# uvicorn main:app --host 0.0.0.0 --port $env:APP_PORT --reload # new
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload # working one
