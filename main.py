from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import candidates, health
from app.core.config import settings
from app.core.database import Base, engine
from app.models import Candidate  # noqa: F401 - registers SQLAlchemy model

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(candidates.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to CareerPilot AI API",
        "docs": "/docs",
        "health": "/health",
    }
