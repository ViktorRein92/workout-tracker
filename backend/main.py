from backend.database import engine, Base, SessionLocal
from backend import models

Base.metadata.create_all(bind=engine)
print("✅ Datenbank bereit!")

def create_session(name: str, notes: str):
    db = SessionLocal() 
    session = models.WorkoutSession(name=name, notes=notes)
    db.add(session)
    db.commit()
    print(f"✅ Trainingseinheit '{name}' angelegt!")
    db.close()

create_session("Pull Day", "Habe Rücken trainiert")


