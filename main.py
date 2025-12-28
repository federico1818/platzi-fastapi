from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hey!"}

country_timezones = {
    "AR": "America/Argentina/Buenos_Aires",
    "MX": "America/Mexico_City",
    "US": "America/New_York",
    "UK": "Europe/London",
}

@app.get("/time/{iso_code}")
async def root(iso_code: str):
    return {
        "time": datetime.now(
            ZoneInfo(country_timezones[iso_code.upper()])
        ).strftime('%H:%M')
    }