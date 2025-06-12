# 🚀 TF-IDF Project Setup Instructions

This document provides clear, step-by-step instructions for deploying and running the TF-IDF web application on your virtual machine.

---

## 📘 English Instructions

### 🔧 Prerequisites:
- Git installed  
- Python 3.11+  
- Internet connection  
- Docker installed and running

---

### 🪜 Step-by-Step Deployment Guide

1. **Create a project folder and enter it**:
   ```bash
   mkdir my_project_folder && cd my_project_folder
   ```

2. **Clone the project**:
   ```bash
   git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects.git
   cd East_Games_Projects/EntranceTask/TF-IDF
   ```

3. **Create and activate a virtual environment** (optional for testing outside Docker):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies** (optional for testing outside Docker):
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup environment and initialize database** (optional if running outside Docker):
   ```bash
   python setup_env.py
   python -m db_schema.db_create
   ```

6. **Build Docker image**:
   ```bash
   sudo docker build -t tf-idf-task3:latest .
   ```

7. **Run Docker container**:
   ```bash
   sudo docker run --name tf-idf-task3 -p 7500:7500 \
     -e APP_PORT=7500 \
     -e UPLOAD_DIR=uploads \
     -e TOP_K_WORDS=50 \
     -e APP_VERSION=3.0.0 \
     -d tf-idf-task3:latest
   ```

8. **Check if the container is running**:
   ```bash
   sudo docker ps
   ```

9. **Open your browser and go to**:
   ```
   http://<your_vm_ip>:7500
   ```

---

## 📗 Инструкция на русском языке

### 🔧 Что потребуется:
- Установленный Git  
- Python 3.11 или новее  
- Подключение к интернету  
- Установленный и работающий Docker

---

### 🪜 Пошаговое руководство по развертыванию

1. **Создайте папку для проекта и перейдите в неё**:
   ```bash
   mkdir my_project_folder && cd my_project_folder
   ```

2. **Клонируйте проект**:
   ```bash
   git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects.git
   cd East_Games_Projects/EntranceTask/TF-IDF
   ```

3. **Создайте и активируйте виртуальное окружение** (опционально, если хотите тестировать без Docker):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Установите зависимости** (опционально, если без Docker):
   ```bash
   pip install -r requirements.txt
   ```

5. **Подготовьте переменные окружения и создайте базу данных** (если не используете Docker):
   ```bash
   python setup_env.py
   python -m db_schema.db_create
   ```

6. **Соберите Docker-образ**:
   ```bash
   sudo docker build -t tf-idf-task3:latest .
   ```

7. **Запустите контейнер Docker**:
   ```bash
   sudo docker run --name tf-idf-task3 -p 7500:7500 \
     -e APP_PORT=7500 \
     -e UPLOAD_DIR=uploads \
     -e TOP_K_WORDS=50 \
     -e APP_VERSION=3.0.0 \
     -d tf-idf-task3:latest
   ```

8. **Проверьте статус контейнера**:
   ```bash
   sudo docker ps
   ```

9. **Откройте в браузере**:
   ```
   http://<your_vm_ip>:7500
   ```
