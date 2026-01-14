from fastapi import FastAPI
app = FastAPI(title="Airbnb Backend")

@app.get("/")
def root():
    return {"status": "ok", "message": "Airbnb backend running"}
