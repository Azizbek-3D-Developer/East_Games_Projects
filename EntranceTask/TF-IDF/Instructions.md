# 🚀 TF-IDF Project Setup Instructions

This document provides clear, step-by-step instructions for deploying and running the TF-IDF web application on your virtual machine.

---

## 📘 English Instructions

### 🔧 Prerequisites:
- Git installed  
- Python 3.11+  
- Docker & Docker Compose installed  
- Internet connection  

---

### 🪜 Step-by-Step Deployment Guide

1. **Create project folder and enter it**:
    ```bash
    mkdir my_project_folder && cd my_project_folder
    ```

2. **Clone the project**:
    ```bash
    git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects.git
    cd EntranceTask/TF-IDF
    ```

3. **Run the special deployment script**:
    ```bash
    python deploy_run.py
    ```

    This will:
    - Install Python packages from `requirements.txt`
    - Create a `.env` file
    - Initialize the database
    - Build and run the Docker container

4. **Check if it is working**  
   Open your browser and go to:

    http://<your_vm_ip>:9000
    

5. **To stop the application**, run this inside the `TF-IDF` folder:
 ```bash
 python deploy_stop.py
 ```

---

## 📗 Инструкция на русском языке

### 🔧 Что потребуется:
- Установленный Git  
- Python 3.11 или новее  
- Docker и Docker Compose  
- Подключение к интернету  

---

### 🪜 Пошаговое руководство по развертыванию

1. **Создайте папку для проекта и перейдите в неё**:
 ```bash
 mkdir my_project_folder && cd my_project_folder
 ```

2. **Клонируйте проект из репозитория**:
 ```bash
 git clone https://github.com/Azizbek-3D-Developer/East_Games_Projects.git
 cd EntranceTask/TF-IDF
 ```

3. **Запустите скрипт развертывания**:
 ```bash
 python deploy_run.py
 ```

 Скрипт выполнит:
 - Установку зависимостей из `requirements.txt`
 - Создание `.env` файла
 - Инициализацию базы данных
 - Сборку и запуск контейнера Docker

4. **Проверьте, что приложение работает**  
Откройте браузер и введите:

    http://<your_vm_ip>:9000

5. **Чтобы остановить приложение**, выполните в папке `TF-IDF`:
 ```bash
 python deploy_stop.py
 ```

---
