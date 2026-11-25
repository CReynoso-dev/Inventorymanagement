from pydantic import BaseModel,ConfigDict,AfterValidator,BeforeValidator,field_validator,Field
from SRC.Custom_Exceptions.Custom_Error import Incorrectcustomernumberlengtherror,Incorrectcustomernumbernxxformaterror
from pydantic_extra_types.phone_numbers import PhoneNumber

class USPhoneNumber(PhoneNumber):
    default_region_code = "US"
    phone_format = "E164"
    phone_format = "NATIONAL"
class CustomerCreate(BaseModel):
    name: str
    number: USPhoneNumber
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