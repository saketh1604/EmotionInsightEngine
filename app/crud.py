from sqlalchemy.orm import Session
from sqlalchemy import desc
from datetime import date, timedelta
from . import models, schemas

def create_mood(db: Session, mood: schemas.MoodCreate):
    existing_mood = db.query(models.Mood).filter(models.Mood.date == mood.date).first()
    if existing_mood:
        existing_mood.mood = mood.mood
        db.commit()
        db.refresh(existing_mood)
        return existing_mood

    db_mood = models.Mood(date=mood.date, mood=mood.mood)
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood

def get_moods(db: Session):
    return db.query(models.Mood).all()

def get_streak(db: Session):
    moods = db.query(models.Mood).order_by(models.Mood.date.desc()).all()

    if not moods:
        return 0

    streak = 1
    previous_date = moods[0].date

    for mood in moods[1:]:
        if previous_date - mood.date == timedelta(days=1):
            streak += 1
            previous_date = mood.date
        else:
            break

    return streak
