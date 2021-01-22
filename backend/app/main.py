from app.api import books, healthcheck
from app.db import database, engine, metadata
from fastapi import FastAPI

metadata.create_all(engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(healthcheck.router)
app.include_router(books.router, prefix="/books", tags=["books"])
