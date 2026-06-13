from fastapi import FastAPI
from backend.database import engine, Base
from backend import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


