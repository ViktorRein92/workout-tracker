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

#create_session("Pull Day", "Habe Rücken trainiert")

def get_sessions():
    db = SessionLocal()
    sessions = db.query(models.WorkoutSession).all()
    db.close()
    return sessions

def print_sessions():
    sessions = get_sessions()
    for s in sessions:
        print(f"✅ ID: {s.id}, Date: {s.date}, Name: {s.name}, Notes: {s.notes}")

print_sessions()
