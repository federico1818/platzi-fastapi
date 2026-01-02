from sqlmodel import Field
from app.models.base.customer_base import CustomerBase

class Customer(CustomerBase, table=True):
    id: int = Field(default=None, primary_key=True)