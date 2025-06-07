from fastapi import APIRouter
from .landing_route import router as landing_route
from .user_register import router as user_register
from .user_login_route import router as user_login
from .user_dashboard_route import router as user_dashboard

api_router = APIRouter()
api_router.include_router(landing_route)
api_router.include_router(user_register)
api_router.include_router(user_login)
api_router.include_router(user_dashboard)