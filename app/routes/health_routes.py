from fastapi import APIRouter

from app.models.healt_check_models import HealthCheck
from app.services.health_services import HealthServices

health_router = APIRouter(prefix="/health", tags=["Health"])

@health_router.get("/")
def get_health_api () -> HealthCheck:
    healt_services = HealthServices()
    return healt_services.get_health()