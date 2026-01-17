from app.models import user
from fastapi import FastAPI
from database import engine, Base

app = FastAPI(
    title="ThinStay Backend",
    description="Local Thai stay & experience booking platform",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "ThinStay backend running"}
