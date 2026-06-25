from fastapi import APIRouter

from modules.dashboard_engine import DashboardEngine

router = APIRouter()

engine = DashboardEngine()


@router.get("/dashboard")
def get_dashboard():

    return engine.get_dashboard()