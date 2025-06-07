# LestaGames_EntranceTask

This repository contains the solution for the **entrance task** provided by **Lesta Games**. The task focuses on building a web application that processes text files, calculates the **TF-IDF** (Term Frequency-Inverse Document Frequency) score for the top 50 words in the file, and displays the results to the user.

---

### 📌 Project Overview

The web application is built using **FastAPI** and **Python**. It includes:
- A form for users to upload text files.
- Processing of the text using **TF-IDF** to calculate word importance.
- Display of the top 50 words with their TF-IDF scores.

The project also features a dark-themed interface with basic styling, allowing users to easily upload their files and view the results in a simple table.

---

### ✅ Features
- **Upload a text file** to the server.
- **Process the file** to calculate the TF-IDF score for each word.
- **Display the top N words** ordered by their TF-IDF scores (configurable).
- **Results page** where users can see the processed words with their respective scores.
- **Dark-themed design** for a sleek and modern user interface.
- **/status** endpoint for health checks.
- **/version** endpoint to return current version info.
- **/metrics** endpoint to track performance and processing stats.

---

### 🛠 Technologies Used
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **scikit-learn**: For calculating TF-IDF scores of the words in the text.
- **Jinja2**: A templating engine to render HTML pages dynamically.
- **python-dotenv**: For managing environment-based configurations.
- **CSS (Custom Styling)**: For the design and layout of the web pages.

---

### 🧠 How It Works
1. **Upload**: The user uploads a text file using the provided form.
2. **Processing**: The server reads the content of the uploaded file and uses **`TfidfVectorizer`** from **scikit-learn** to calculate the TF-IDF scores of the words.
3. **Display**: The top N words, sorted by their TF-IDF scores, are displayed in a table on a results page.
4. **Monitoring**: System endpoints allow version checking, application health status, and performance metrics.

---
### Project DataBase Structure
📘 [View Database Schema](db_schema/DB_STRUCTURE.md)

---
### 📁 Project Structure

├── main.py # FastAPI application
├── requirements.txt # Project dependencies
├── .env # Environment variables (not committed)
├── static/ # Static files (CSS, JS, etc.)
├── Templetes/ # HTML templates (upload.html, results.html)
├── uploads/ # Uploaded text files
└── README.md # Project documentation


---

### ⚙️ Configuration via `.env`

The following environment variables can be configured in a `.env` file in the root folder:

```env
APP_PORT=8000                # Port where the app runs
APP_VERSION=1.1.0            # Application version
UPLOAD_DIR=uploads           # Directory to save uploaded files
TOP_K_WORDS=50               # Number of top TF-IDF words to display


---

### 🚀 Setup and Installation

# 1. Clone the repository
git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects
cd EntranceTask/TF-IDF

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file in the root directory (optional, default values are used if missing)

# 4. Run the app
uvicorn main:app --reload

# 5. Result
Access the app at: http://127.0.0.1:8000




### Available end-points
🔍 Available Endpoints
Endpoint	Method	Description
/	GET	Main upload page
/upload	POST	Uploads and processes a file
/status	GET	Returns { "status": "OK" }
/version	GET	Returns { "version": "1.1.0" }
/metrics	GET	Returns processing performance stats


---

### 📜 Changelog

See the [CHANGELOG.md](./CHANGELOG.md) file for detailed version history and updates.


## Docker Build & Run (if you have Docker)

To build the Docker image, run:

```bash
docker build -t tfidf-app .


### To run the container and expose it on port 8000:
docker run -p 8000:8000 tfidf-app
