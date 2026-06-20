from fastapi import FastAPI

app = FastAPI(
    title="MCPShield",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "MCPShield API Running"
    }