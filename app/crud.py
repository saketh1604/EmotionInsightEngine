from sqlalchemy.orm import Session
from . import models, schemas

def create_mood(db: Session, mood: schemas.MoodCreate):
    db_mood = models.Mood(date=mood.date, mood=mood.mood)
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood

def get_moods(db: Session):
    return db.query(models.Mood).all()
