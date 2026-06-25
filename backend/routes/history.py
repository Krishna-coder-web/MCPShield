from fastapi import APIRouter

from modules.history_engine import HistoryEngine

router = APIRouter()

engine = HistoryEngine()


@router.get("/history",include_in_schema=False)
def get_history():

    return engine.get_history()

@router.get("/recent",include_in_schema=False)
def get_recent():

    return engine.get_recent()