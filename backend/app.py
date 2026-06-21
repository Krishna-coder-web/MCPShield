from fastapi import FastAPI

from routes.scan import router as scan_router

app = FastAPI(
    title="MCPShield",
    version="1.0.0"
)

app.include_router(scan_router)


@app.get("/")
def root():
    return {
        "message": "MCPShield API Running"
    }