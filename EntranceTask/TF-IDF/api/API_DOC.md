# API Module Documentation

This folder contains all API-related logic for the project. It follows a modular design pattern to separate concerns and keep the code maintainable.

---

## 📁 File Structure

- `routes/_route.py` — FastAPI route definitions  
- `crud/_crud.py` — Database operations (CRUD logic)  
- `schemas/_schema.py` — Pydantic models for request/response validation  

---

## 🚀 How to Use

1. **Register routes in `__init__.py` inside of the routes folder:**

   ```python
   from fastapi import APIRouter
   from .LandingPage.landing_route import router as landing_route
   api_router = APIRouter()
   
   api_router.include_router(landing_route)
   ```

---

## Dependencies

- FastAPI
- SQLAlchemy
- Databases
- Pydantic

---
