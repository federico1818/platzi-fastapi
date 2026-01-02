from fastapi import FastAPI, Depends
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlmodel import Session, select
from app.db.session import create_db, get_session
from app.models.orm.customer import Customer
from app.schemas.customer_create_schema import CustomerCreateSchema

app = FastAPI(lifespan=create_db)

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
async def time(iso_code: str):
    return {
        "time": datetime.now(
            ZoneInfo(country_timezones[iso_code.upper()])
        ).strftime('%H:%M')
    }

@app.post("/customers")
async def create_customer(customer_create_schema: CustomerCreateSchema, session: Session = Depends(get_session)):
    customer = Customer.from_orm(customer_create_schema)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.get("/customers", response_model=list[Customer])
async def get_customers(session: Session = Depends(get_session)):
    return session.exec(select(Customer)).all()