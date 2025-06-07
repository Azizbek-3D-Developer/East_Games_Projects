# API Module Documentation

This folder contains all API-related logic:

- `routes.py` — FastAPI route definitions
- `crud.py` — Database operations for CRUD
- `schemas.py` — Pydantic models for data validation

## How to use

- Import `api.routes` in main.py and include router
- Add new endpoints in `routes.py`
- Put database interaction code in `crud.py`
- Define request/response models in `schemas.py`

## Adding new endpoints

1. Define route function in `routes.py`
2. Create or update schema in `schemas.py`
3. Write DB queries in `crud.py`

## Dependencies

- FastAPI
- SQLAlchemy
- Databases
- Pydantic

...
