from fastapi import FastAPI

app = FastAPI(
    title="ThinStay Backend",
    description="Local Thai stay & experience booking platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "ThinStay Backend"
    }
