from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CandidateCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    education: str = Field(default="", max_length=500)
    experience_years: float = Field(default=0, ge=0, le=60)
    career_goal: str = Field(default="", max_length=500)
    location: str = Field(default="", max_length=120)
    skills: list[str] = Field(default_factory=list, max_length=40)
    interests: list[str] = Field(default_factory=list, max_length=40)


class CandidateResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    education: str
    experience_years: float
    career_goal: str
    location: str
    skills: list[str]
    interests: list[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
