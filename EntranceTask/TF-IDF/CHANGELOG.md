# Changelog

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
