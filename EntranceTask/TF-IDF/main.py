# Azizbek Axmatjonov
# Project based on task Provided by Nargiza Ruzaeva (Recruiter of Lesta Games) Time: 02.05.2025

# Libraries
from fastapi import FastAPI, Request, UploadFile, File # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
import shutil, os
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore

# Main Variables Setup
app = FastAPI()

# Static items folder root
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja framework used for rendering HTML files
templates = Jinja2Templates(directory="Templetes")

# Creating upload directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Default link called
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request}) # Landing page of the Application

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with open(file_location, "r", encoding="utf-8") as f:
        text = f.read()

    vectorizer = TfidfVectorizer()   # TfidfVectorizer instance
    X = vectorizer.fit_transform([text])
    tfidf_scores = dict(zip(vectorizer.get_feature_names_out(), X.toarray()[0]))

    sorted_words = sorted(tfidf_scores.items(), key=lambda x: -x[1])[:50]  # getting top 50 words

    # redirecting user to the results page
    return templates.TemplateResponse("results.html", {
        "request": request,
        "results": sorted_words
    })


# runing code
# pip install -r requirements.txt
# uvicorn main:app --reload