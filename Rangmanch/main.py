from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from db_config import get_session, create_table



@asynccontextmanager
async def app_lifespan(app:FastAPI):
    create_table()
    print("DB tables created")
    yield
    print("Shutting down the app")


app = FastAPI(
    title="RangManch APP",
    description="An theatre booking App.",
    lifespan=app_lifespan
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000, host="127.0.0.1")
    