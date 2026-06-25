from fastapi import FastAPI

from routes.scan import router as scan_router
from routes.stats import router as stats_router
from routes.history import router as history_router
from routes.dashboard import router as dashboard_router

app = FastAPI(
    title="MCPShield",
    version="1.0.0"
)

app.include_router(scan_router)
app.include_router(dashboard_router)
app.include_router(stats_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {
        "message": "MCPShield API Running"
    }