
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

from backend.api import app as api


app = FastAPI(
    title="Credit Card Validation API",
    description="API for fast validation of credit cards"
)

app.mount("/app", StaticFiles(directory="./frontend", html=True), name="frontend")

app.include_router(api)


if __name__ == "__main__":
    uvicorn.run("main:app", port=7001)
