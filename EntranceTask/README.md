# 🎮 LestaGames Entrance Task / Входное задание LestaGames

This repository contains the solution to the **entrance task** provided by **Lesta Games**.  
В этом репозитории находится решение **входного задания**, предоставленного **Lesta Games**.

The task involves building a web application that processes uploaded text files, calculates the **TF-IDF** (Term Frequency-Inverse Document Frequency) scores, and displays the top words.  
Задача заключается в создании веб-приложения, которое обрабатывает загруженные текстовые файлы, вычисляет **TF-IDF** и отображает наиболее важные слова.

---

## 📌 Project Overview / Обзор проекта

The web app is built with **FastAPI** and **Python**, and uses **Jinja2** for HTML rendering.  
Веб-приложение построено на **FastAPI** и **Python**, с использованием **Jinja2** для отображения HTML.

---

## ✅ Features / Функциональность

- 🔐 **User Registration / Регистрация пользователей**
- 🔑 **User Login / Авторизация с JWT (1 час)**
- 📂 **File Upload / Загрузка файлов `.txt`**
- 📊 **TF-IDF Calculation / Расчёт TF-IDF с помощью scikit-learn**
- 🏆 **Top 50 Words / Отображение топ-50 слов**
- 📈 **Result Page / Страница с результатами и визуализацией**
- 🌙 **Dark Theme / Современный тёмный UI**
- 🗂 **Collections / Создание коллекций и назначение документов**

---

## 📄 Documentation Links / Ссылки на документацию

- 📘 [**Project Routes**](TF-IDF/api/routes/ROUTES.md) – API endpoints  
  📘 **Маршруты проекта**

- 📘 [**API Folder Instructions**](TF-IDF/api/API_DOC.md) – Folder structure & usage  
  📘 **Описание структуры API**

- 📘 [**Database Schema**](TF-IDF/db_schema/DB_STRUCTURE.md) – Tables and relations  
  📘 **Структура базы данных**

- 📜 [**CHANGELOG.md**](TF-IDF/CHANGELOG.md) – Version history  
  📜 **История версий и изменений**

- 📜 [**Instructions.md**](TF-IDF/Instructions.md) – How to install and run the project  
  📜 **Инструкция по запуску и установке**

---

## 🛠 Technologies Used / Используемые технологии

- ⚡ **FastAPI** – High-performance backend framework  
- 🧠 **scikit-learn** – TF-IDF vectorizer and stats  
- 🖼 **Jinja2** – HTML templating engine  
- 📦 **python-dotenv** – Manage environment config  
- 🎨 **CSS** – Custom dark theme and layout

---

## 🧠 How It Works / Как это работает

1. 📤 **Upload** – User uploads a `.txt` file  
   👤 Пользователь загружает `.txt` файл

2. ⚙️ **Processing** – App computes TF-IDF with `TfidfVectorizer`  
   📊 Приложение рассчитывает TF-IDF с помощью `TfidfVectorizer`

3. 🖥 **Display** – Results shown on a visual summary page  
   📈 Результаты отображаются на отдельной странице

4. 🩺 **Monitoring** – App health, version, and metrics endpoints  
   🩺 Эндпоинты для проверки состояния, версии и метрик

---

## 🚀 Deployment Help / Развёртывание

To deploy and run the project on a virtual machine, follow the instructions in:  
📘 [**Instructions.md**](TF-IDF/Instructions.md)

Для развёртывания проекта на виртуальной машине, следуйте инструкции в:  
📘 [**Instructions.md (русская версия включена)**](TF-IDF/Instructions.md)

---

## 💬 Feedback / Обратная связь

If you’ve cloned and tested this project, feel free to leave feedback in the `VISITOR_FEEDBACK.md`!  
Если вы запускали этот проект, не забудьте оставить отзыв в `VISITOR_FEEDBACK.md`! в папке EntranceTask

---
