from fastapi import FastAPI

from src.staff.routes import staff_router
from src.staff_schedule.routes import staff_schedule_router


version = "v1"
api_url_prefix = f"/api/{version}"

app = FastAPI(
    title="Electronic Hospital Resource Management",
    description="Electronic Hospital Resource Management App manages and improves the performance of activities in the hospital.",
    version=version,
    docs_url=f"/api/{version}/docs",
    redoc_url=f"/api/{version}/redoc",
    openapi_url=f"/api/{version}/openapi.json",
    contact={
        "name": "Ikechukwu Okoro",
        "email": "ikeshegs@gmail.com"
    }
)

@app.get("f{api_url_prefix}")
async def root():
    return {"message": "Welcome to Electronic Hospital Resource Management App"}

app.include_router(staff_router, prefix=f"{api_url_prefix}/staff", tags=["Staff"])
app.include_router(staff_schedule_router, prefix=f"{api_url_prefix}/staff/schedule", tags=["Staff Schedule"])
