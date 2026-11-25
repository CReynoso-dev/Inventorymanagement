from pydantic import BaseModel,ConfigDict,AfterValidator,BeforeValidator,field_validator,Field
from SRC.Custom_Exceptions.Custom_Error import Incorrectcustomernumberlengtherror,Incorrectcustomernumbernxxformaterror
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import EmailStr

class USPhoneNumber(PhoneNumber):
    default_region_code = "US"
    phone_format = "NATIONAL"
class CustomerCreate(BaseModel):
    name: str
    number: USPhoneNumber
    email: EmailStr
    timewith: int = Field(ge=0)
    model_config = ConfigDict(from_attributes=True)
class CustomerDelete(BaseModel):
    pass

class ProductDelete(BaseModel):
    pass

class CustomerUpdate(BaseModel):
    name: str | None = None
    number: USPhoneNumber | None = None
    email: EmailStr | None = None
    timewith: int | None = None
    model_config = ConfigDict(from_attributes=True)

class ProductCreate(BaseModel):
    upc: str
    name: str
    quantity: int
    price: int
    description: str
    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    upc: str | None = None
    name: str | None = None
    quantity: int | None = None
    price: int | None = None
    description: str | None = None
    model_config = ConfigDict(from_attributes=True)