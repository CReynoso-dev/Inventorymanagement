import uuid

from pydantic import BaseModel

class Customer(BaseModel):
    customer_id : uuid.UUID
    name : str
    number : str
    email : str
    timewith : int
class Product(BaseModel):
    product_id : uuid.UUID
    upc : str
    name : str
    quantity : int
    price : int
    description : str