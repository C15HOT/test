from fastapi import FastAPI
from uvicorn import run

app = FastAPI(
    title="test",
    description="",
)

from app.routes.test_router import test_router

app.include_router(test_router)


def main() -> None:
    run(
        app,
        host='0.0.0.0',
        port=8080
    )
