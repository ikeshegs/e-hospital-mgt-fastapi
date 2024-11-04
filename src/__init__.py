from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.staff.router import staff_router
from src.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()


version = "v1"

app = FastAPI(
    title="Electronic Hospital Resources Management",
    description="Electronic",
    version=version,
    docs_url=f"/api/{version}/docs",
    redoc_url=f"/api/{version}/redoc",
    openapi_url=f"/api/{version}/openapi.json",
    lifespan=lifespan,
    contact={
        "name": "Ikechukwu Okoro",
        "email": "ikeshegs@gmail.com"
    }
)

@app.get("/")
async def root():
    return {"message": "Welcome to E-Hospital Management System"}

app.include_router(staff_router, prefix=f"/api/{version}/staff", tags=["Staff"])
