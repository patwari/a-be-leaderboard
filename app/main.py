from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.base import Base
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs on startup
    Base.metadata.create_all(bind=engine)
    yield
    # Runs on shutdown (optional cleanup)


app = FastAPI(lifespan=lifespan)


@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}
