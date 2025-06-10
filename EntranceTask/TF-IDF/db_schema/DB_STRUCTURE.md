# Azizbek Axmatjonov TF_IDF Project
# 🧱 Database Structure

This document outlines the planned database schema for the TF-IDF Web Application.

---

## 👤 Users
Stores system users who can upload and manage documents and collections.

| Field         | Type     | Description                     |
|---------------|----------|---------------------------------|
| id            | Integer  | Primary key                     |
| email         | String   | Unique eamil                    |
| username      | String   | Unique username                 |
| password_hash | String   | Hashed password                 |
| created_at    | DateTime | Account creation timestamp      |

---

## 📄 Documents
Stores metadata for uploaded text files.

| Field      | Type     | Description                        |
|------------|----------|------------------------------------|
| id         | Integer  | Primary key                        |
| filename   | String   | Original name of uploaded file     |
| filecontent| String   | Original string of uploaded file   |
| path       | String   | File storage path on server        |
| user_id    | Integer  | FK to Users.id                     |
| uploaded_at| DateTime | Upload timestamp                   |

---

## 📦 Collections
Groups of documents under a common user.

| Field      | Type     | Description                        |
|------------|----------|------------------------------------|
| id         | Integer  | Primary key                        |
| name       | String   | Name of the collection             |
| user_id    | Integer  | FK to Users.id                     |
| created_at | DateTime | Creation timestamp                 |

---

## 🔗 CollectionDocuments
Links documents to collections (many-to-many relationship).

| Field         | Type    | Description                        |
|---------------|---------|------------------------------------|
| collection_id | Integer | FK to Collections.id               |
| document_id   | Integer | FK to Documents.id                 |

---

## 📊 Statistics
Stores TF-IDF results for a document or aggregated per collection.

| Field         | Type     | Description                           |
|---------------|----------|---------------------------------------|
| id            | Integer  | Primary key                           |
| document_id   | Integer  | FK to Documents.id                    |
| tfidf_json    | JSON     | List of top 50 words with TF and IDF  |
| created_at    | DateTime | When stats were computed              |

---

## 📊 Metrics  
Stores aggregated processing metrics for uploaded files, including processing times and custom statistics.

| Field                        | Type     | Description                                              |
|------------------------------|----------|----------------------------------------------------------|
| id                           | Integer  | Primary key, always `1` (singleton row)                   |
| files_processed              | Integer  | Total number of files processed by the application        |
| min_time_processed          | Float    | Minimum processing time per file (seconds, 3 decimals)    |
| avg_time_processed          | Float    | Average processing time per file (seconds, 3 decimals)    |
| max_time_processed          | Float    | Maximum processing time per file (seconds, 3 decimals)    |
| latest_file_processed_timestamp | DateTime | Timestamp of the most recent file processing               |
| total_upload_size_bytes     | Integer  | Sum of sizes (in bytes) of all uploaded files             |
| last_uploaded_filename      | String   | Filename of the most recently uploaded file               |

---



## ⚠️ Notes
- A document may belong to **multiple collections**.
- IDF is shared within a collection.
- User deletion should cascade to documents, collections, and statistics.

---

## 📁 UML Diagram
#### See the UML diagram files here:  
- 📁 [Db_Schema.drawio](./TF-IDF/db_schema/Db_Schema.drawio)  
- 🖼️ [Db_Schema.jpg](./TF-IDF/db_schema/Db_Schema.jpg)  


---