from pydantic import BaseModel,ConfigDict



class CustomerCreate(BaseModel):
    name: str
    number: str
    email: str
    timewith: int
    model_config = ConfigDict(from_attributes=True)

class CustomerUpdate(BaseModel):
    name: str | None
    number: str | None
    email: str | None
    timewith: int | None
    model_config = ConfigDict(from_attributes=True)

class ProductCreate(BaseModel):
    upc: str
    name: str
    quantity: int
    price: int
    description: str
    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    upc: str | None
    name: str | None
    quantity: int | None
    price: int | None
    description: str | None
    model_config = ConfigDict(from_attributes=True)