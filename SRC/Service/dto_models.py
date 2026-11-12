from pydantic import BaseModel,ConfigDict
import uuid


class ProductDTO(BaseModel):
    product_id: uuid.UUID
    upc: str
    name: str
    quantity: int
    price: int
    description: str
    model_config = ConfigDict(from_attributes=True)
class CustomerDTO(BaseModel):
    customer_id: uuid.UUID
    name: str
    number: str
    email: str
    timewith: int
    model_config = ConfigDict(from_attributes=True)