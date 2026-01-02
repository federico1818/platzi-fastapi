from typing import Annotated
from sqlmodel import Session, create_engine, SQLModel
from fastapi import FastAPI, Depends

name = "db.sqlite3"
engine = create_engine(f"sqlite:///{name}")

def create_db(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session() -> Annotated[Session, Depends]:
    with Session(engine) as session:
        yield session