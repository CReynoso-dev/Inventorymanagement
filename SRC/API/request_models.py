from pydantic import BaseModel,ConfigDict



class CustomerCreate(BaseModel):
    name: str
    number: str
    email: str
    timewith: int
    model_config = ConfigDict(from_attributes=True)




class ProductCreate(BaseModel):
    upc: str
    name: str
    quantity: int
    price: int
    description: str
    model_config = ConfigDict(from_attributes=True)