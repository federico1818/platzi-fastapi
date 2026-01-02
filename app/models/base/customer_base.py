from sqlmodel import Field, SQLModel

class CustomerBase(SQLModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)