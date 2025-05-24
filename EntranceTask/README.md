# LestaGames_EntranceTask

This repository contains the solution for the **entrance task** provided by **Lesta Games**. The task focuses on building a web application that processes text files, calculates the **TF-IDF** (Term Frequency-Inverse Document Frequency) score for the top 50 words in the file, and displays the results to the user.

### Project Overview

The web application is built using **FastAPI** and **Python**. It includes:
- A form for users to upload text files.
- Processing of the text using **TF-IDF** to calculate word importance.
- Display of the top 50 words with their TF-IDF scores.

The project also features a dark-themed interface with basic styling, allowing users to easily upload their files and view the results in a simple table.

### Features
- **Upload a text file** to the server.
- **Process the file** to calculate the TF-IDF score for each word.
- **Display the top 50 words** ordered by their TF-IDF scores.
- **Results page** where users can see the processed words with their respective scores.
- **Dark-themed design** for a sleek and modern user interface.

### Technologies Used
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **scikit-learn**: For calculating TF-IDF scores of the words in the text.
- **Jinja2**: A templating engine to render HTML pages dynamically.
- **CSS (Custom Styling)**: For the design and layout of the web pages.

### How It Works
1. **Upload**: The user uploads a text file using the provided form.
2. **Processing**: The server reads the content of the uploaded file and uses **`TfidfVectorizer`** from **scikit-learn** to calculate the TF-IDF scores of the words.
3. **Display**: The top 50 words, sorted by their TF-IDF scores, are displayed in a table on a results page.

### Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects
   cd EntranceTask
   cd TF-IDF
   pip install -r requirements.txt
   uvicorn main:app --reload

