from fastapi import APIRouter
from .LandingPage.landing_route import router as landing_route
from .LandingPage.user_register import router as user_register
from .LandingPage.user_login_route import router as user_login
from .user_dashboard_route import router as user_dashboard
from .documents_route import router as user_documents_route
from .statistics_route import router as user_statistics_route
from .custom_routes.status_route import router as tf_idf_status_route
from .collections_route import router as user_collection_route
from .custom_routes.metrics_routes import router as metrics_router

api_router = APIRouter()

api_router.include_router(landing_route)
api_router.include_router(user_register)
api_router.include_router(user_login)
api_router.include_router(user_dashboard)
api_router.include_router(user_documents_route)
api_router.include_router(user_statistics_route)
api_router.include_router(tf_idf_status_route)
api_router.include_router(user_collection_route)
api_router.include_router(metrics_router)



