# Changelog

All notable changes to this project will be documented in this file.

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

## [1.0.0] - 2025-05-02
### Initial release
- Basic FastAPI web app for uploading text files.
- TF-IDF computation for top 50 words.
- Display results on a dynamically rendered results page.
- Basic styling and UI for ease of use.
