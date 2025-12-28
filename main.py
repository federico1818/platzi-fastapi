from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hey!"}

@app.get("/time")
async def root():
    return {"time": datetime.now().strftime('%H:%M')}