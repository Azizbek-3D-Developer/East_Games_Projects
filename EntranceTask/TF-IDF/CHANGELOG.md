# Changelog

***
Обратная связь по проекту.

Заполняю в Changelog как установлено в задании.

Понравилось как реализовал внешнюю часть проекта. Видно, что подходил с желанием и старался внешне выделить проект. 
Много эффектов, есть прикольные анимации (например на 404). Своего рода RGB подсветка.
На странице можно сразу получить всю информацию (статистики, контент и т.д). Работает быстро. Загружал достаточно
большой текст и моментально получил всю информацию. Это прикольно. Не понял почему можно создать пользователя
только с gmail аккаунтом.

По старту проекта были небольшие проблемы. Если следовать инструкции и попробовать запустить образ приложения, то запуск
не успешен, т.к. в пункте 5 инструкции есть команды для создания .env файла (это тоже понравилось - удобно), и создания 
БД, с указанием если не используете Docker, но докер-файл не запускает эти команды, т.е. их нужно выполнить даже при
запуске через докер. Не хватило описания переменных окружения и сами переменные остались не очень понятными для меня. В 
приложении используется SQLite, но настройка переменных указывает на Postgres. Но если использовать Postgres,
то докер-компоуз не поднимает эту БД.

На что бы я обратил внимание:
1. На архитектуру проекта.
- У проекта большая вложенность 
  - East_Games_Projects - папка с README и еще папкой
  - EntranceTask - папка с еще одним README и еще папкой
  - TF-IDF - сам проект
  - Разделение логики. Например, в папке LandingPage находится логика логина и регистрации, а другие действия с 
  пользователем, находятся в файле user_dashboard_route.py, вне этой папки.
  - В проекте много неиспользуемых импортов и переменных
2. Нэйминг файлов и папок. 
  - Выше видно, что три папки названы разными стилями
  - Это есть во всем проекте (snake case, camel case)
3. Неявная точка входа в приложение. В корне есть app.py, но в папке old_files (?) есть main.py, что тоже может быть
точкой входа. Там даже создается экземпляр приложения.
4. В requirements.txt много лишних зависимостей, которые подтягиваются при установке основных. Указаны версии - это хорошо.
5. В .gitignore добавлена папка .idea, но она запушена

# Сам API
На что бы обратил внимание:
- Все эндпоинты располагаются в одной группе default, что значительно усложняет работу с ними.
- Не хватило документации для эндпоинтов. Ее нет. Например, для /login есть два эндпоинта - GET и POST. Без описания и
группировки сложно сразу понять что делает каждый и в чем между ними разница.
- Используется только два типа запросов (кроме одного случая) - GET и POST.
- Эндпоинт смены данных пользователя использует PUT запрос. Такой запрос меняет все поля. (Через этот запрос можно менять
регистрационные данные любого пользователя. Я смог изменить данные пользователя на сервере с id 2 без регистрации)
- Во всем API ошибка, которая рассматривалась в лекции по Swagger. Все эндпоинты возвращают HTMLResponse.

### От себя:
Считаю, что приложено много усилий и стараний в проект, чтобы не только все работало, но и выделялось и запоминалось.
Эта цель выполнена, работает быстро, выглядит эффектно.
Дополнительно, я бы порекомендовал больше времени уделять чтению и изучению технического задания от заказчика.
Например, в задании первой недели: 
```
2.2.1.1.
/status
возвращает json {“status”: “OK”}, если всё хорошо. Отсутствие ответа будем
считать индикацией того, что приложение работает с ошибками.
```
А текущая версия API возвращает страницу HTML...

Сам проект мне понравился, думаю, что ты очень старался. Выглядит и работает очень прикольно.
***

All notable changes to this project will be documented in this file.

## [2.1.0] - 2025-06-12

### Added

- Completed Huffman coding feature:
  - `/dashboard/documents/{document_id}/huffman` endpoint now renders Huffman encoding data.
  - Huffman model added to `models/huffman.py`.
  - Pydantic schema and service logic added for Huffman encoding and storage.
  - Database support for Huffman encoding results.


- JavaScript toggle scripts for section collapsibility.

---

## [2.0.0] - Total restructure of the project – 2025-06-08

### Folders added

- **api**
  - auth/
  - utils/
  - schemas/
  - crud/
  - services/

- **db_schema**
  - db_create.py
  - Db_Schema.drawio
  - Db_Schema.jpg
  - testing_db.py

- **models**
  - user.py
  - collection.py
  - document.py
  - statistics.py
  - collection_document.py

- **static**
  - images/
    - Alucard.jpg
    - bg.jpg
  - scripts/
    - landing-page-script.js
  - styles/
    - Dashboard/
      - Collections/
        - collections-styles.css
      - Documents/
        - documents-styles.css
      - Statistics/
        - statistics-styles.css
      - dashboard-styles.css
    - LandingPage/
      - landing-styles.css
      - login-styles.css
      - register-styles.css
      - status-styles.css
    - base-styles.css
    - error-styles.css
  - Styles-design.md

- **templates**
  - Dashboard/
    - Collections/
      - collection-create.html
      - collection-update.html
      - collection-details.html
      - collection.html
    - documents/
    - statistics/
  - LandingPage/
  - old/
    - base.html
    - error-404.html
    - error-500.html

- app.py — *new starting point of the application*

- .gitignore

---

### Features
- New route documentation file created with detailed grouping of all project endpoints (public and authenticated).
- Document Details page now includes:
  - Visually separated and collapsible sections for:
    - Document metadata
    - TF-IDF statistics
    - Associated collections
    - Add-to-collection form
- Collection Details page enhanced:
  - Matching collapsible structure for consistency.
  - Uses separate CSS for desktop and mobile.
  - Dynamic listing of documents within a collection.
- Fully responsive layout styles for `statistics_detail.html`, `collection-details.html`, and `document-details.html`.
---

## [1.1.0] - 2025-05-26

### Added
- Support for configuration via `.env` file: upload directory, top K TF-IDF words count, and app version.
- New endpoints added:
  - `/status` — returns application health status.
  - `/version` — returns current application version.
  - `/metrics` — returns processing statistics and performance metrics.
- Added processing time tracking per file upload.
- Refined TF-IDF processing to support configurable number of top words.
- Dark-themed user interface improvements.

---

## [1.0.0] - 2025-05-02

### Initial release
- Basic FastAPI web app for uploading text files.
- TF-IDF computation for top 50 words.
- Display results on a dynamically rendered results page.
- Basic styling and UI for ease of use.
