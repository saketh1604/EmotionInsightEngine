from pydantic import BaseModel
from datetime import date

class MoodCreate(BaseModel):
    date: date
    mood: str

class Mood(BaseModel):
    id: int
    date: date
    mood: str

    class Config:
        orm_mode = True

class MoodStreak(BaseModel):
    streak_count: int
