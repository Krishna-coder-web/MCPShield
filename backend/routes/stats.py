from fastapi import APIRouter

from modules.stats_engine import StatsEngine

router = APIRouter()

stats_engine = StatsEngine()

@router.get("/stats")
def get_stats():

    return stats_engine.get_stats()