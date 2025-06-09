# LestaGames Entrance Task

This repository contains the solution to the **entrance task** provided by **Lesta Games**. The task involves building a web application that processes uploaded text files, calculates the **TF-IDF** (Term Frequency-Inverse Document Frequency) scores, and displays the top words based on these scores.

---

### 📌 Project Overview

The web application is built using **FastAPI** and **Python**, with **Jinja2** for HTML rendering.

---

### ✅ Features

- **User Registration** – Create a new user account.
- **User Login** – Authenticate and receive a JWT token (valid for 1 hour).
- **File Upload** – Upload `.txt` files for processing.
- **TF-IDF Calculation** – Compute the TF-IDF scores of words using `scikit-learn`.
- **Top 50 Words Display** – View the highest-ranked words based on TF-IDF scores.
- **Result Page** – Visual presentation of word statistics and scores.
- **Dark Theme** – Modern, user-friendly dark UI.
- **Collections Support** – Users can create collections and assign documents to them.

---

## Links to documents

#### See 📘 [Project Routes](TF-IDF/api/routes/ROUTES.md) for available routes
---

#### See 📘 [API Folder Instructions](TF-IDF/api/API_DOC.md) for api folder content and how to work with them
---

#### See 📘 [Database Schema](TF-IDF/db_schema/DB_STRUCTURE.md) for database structure and tables
---

#### See 📜 [CHANGELOG.md](TF-IDF/CHANGELOG.md) for version history and development updates.
---

#### See 📜 [Instructions.md](TF-IDF/Instructions.md) for project runing and installing guides

### 🛠 Technologies Used

- **FastAPI** – High-performance Python web framework.
- **scikit-learn** – For computing TF-IDF scores.
- **Jinja2** – Template engine for rendering HTML.
- **python-dotenv** – Manage environment variables.
- **CSS** – Custom styling for frontend UI.

---

### 🧠 How It Works

1. **Upload** – Users upload a `.txt` file using a web form.
2. **Processing** – Server extracts content and computes TF-IDF scores using `TfidfVectorizer`.
3. **Display** – Results are shown on a dedicated results page, highlighting the top N words.
4. **Monitoring** – Endpoints provide application health status, version info, and performance metrics.

---




