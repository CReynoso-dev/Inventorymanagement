import uuid

from pydantic import BaseModel

class Customer(BaseModel):
    customer_id : uuid.UUID
    name : str
    number : str
    email : str
    timewith : int
