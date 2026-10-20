import uuid

from pydantic import BaseModel,ConfigDict

class CustomerResponse(BaseModel):
    customer_id: uuid.UUID
    name: str
    number: str
    email: str
    timewith: int
    model_config = ConfigDict(from_attributes=True)
class ProductResponse(BaseModel):
    product_id: uuid.UUID
    upc: str
    name: str
    quantity: int
    price: int
    description: str
    model_config = ConfigDict(from_attributes=True)
