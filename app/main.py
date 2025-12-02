from fastapi import FastAPI, Depends
from . import models, schemas, crud, database
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Emotion Insight Engine")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/moods")
def add_mood(mood: schemas.MoodCreate, db: Session = Depends(database.get_db)):
    return crud.create_mood(db, mood)

@app.get("/moods")
def list_moods(db: Session = Depends(database.get_db)):
    return crud.get_moods(db)

@app.get("/moods/streak")
def get_streak(db: Session = Depends(database.get_db)):
    streak = crud.get_streak(db)
    return {"streak_count": streak}
