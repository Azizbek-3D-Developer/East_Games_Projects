# 🚀 TF-IDF Project Setup Instructions

This document provides clear, step-by-step instructions for deploying and running the TF-IDF web application on your virtual machine.

---

## 📘 English Instructions

### 🔧 Prerequisites:
- Git installed  
- Python 3.11+  
- Internet connection  

---

### 🪜 Step-by-Step Deployment Guide (No Docker)

1. **Create a project folder and enter it**:
   ```bash
   mkdir my_project_folder && cd my_project_folder
   ```

2. **Clone the project**:
   ```bash
   git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects.git
   cd East_Games_Projects/EntranceTask/TF-IDF
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the deployment script**:
   ```bash
   python3 deploy_run.py
   ```

   This will:
   - Create a `.env` file (if needed)
   - Initialize the database
   - Start the app with Uvicorn

6. **Check if it is working**  
   Open your browser and go to:

   ```
   http://<your_vm_ip>:9000
   ```

7. **To stop the application**, press `Ctrl+C` in the terminal or use:
   ```bash
   python3 deploy_stop.py
   ```

---

## 📗 Инструкция на русском языке

### 🔧 Что потребуется:
- Установленный Git  
- Python 3.11 или новее  
- Подключение к интернету  

---

### 🪜 Пошаговое руководство по развертыванию (без Docker)

1. **Создайте папку для проекта и перейдите в неё**:
   ```bash
   mkdir my_project_folder && cd my_project_folder
   ```

2. **Клонируйте проект**:
   ```bash
   git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects.git
   cd East_Games_Projects/EntranceTask/TF-IDF
   ```

3. **Создайте и активируйте виртуальное окружение**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Запустите скрипт развертывания**:
   ```bash
   python3 deploy_run.py
   ```

   Скрипт выполнит:
   - Создание файла `.env` (если он отсутствует)
   - Инициализацию базы данных
   - Запуск приложения через Uvicorn

6. **Проверьте работу приложения**  
   Откройте браузер и перейдите по адресу:

   ```
   http://<your_vm_ip>:9000
   ```

7. **Остановить приложение** можно с помощью `Ctrl+C` в терминале или команды:
   ```bash
   python3 deploy_stop.py
   ```
