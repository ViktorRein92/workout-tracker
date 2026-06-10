from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(DateTime, default=datetime.now)
    notes = Column(String, nullable=True)

    exercises = relationship("Exercise", back_populates="session")

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    muscle_group = Column(String, nullable=False)
    session_id = Column(Integer, ForeignKey("workout_sessions.id"))

    session = relationship("WorkoutSession", back_populates="exercises")
    sets = relationship("SetEntry", back_populates="exercise")


class SetEntry(Base):
    __tablename__ = "set_entries"

    id = Column(Integer, primary_key=True, index=True)
    set_number = Column(Integer, nullable=False)
    weight_kg = Column(Float, nullable=False)
    reps = Column(Integer, nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"))

    exercise = relationship("Exercise", back_populates="sets")

