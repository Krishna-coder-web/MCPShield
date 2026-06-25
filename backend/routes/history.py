from fastapi import APIRouter

from modules.history_engine import HistoryEngine

router = APIRouter()

engine = HistoryEngine()


@router.get("/history")
def get_history():

    return engine.get_history()

@router.get("/recent")
def get_recent():

    return engine.get_recent()