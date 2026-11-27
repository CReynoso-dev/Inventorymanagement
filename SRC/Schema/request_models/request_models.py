
from pydantic import BaseModel,ConfigDict,Field,model_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import EmailStr,UUID4
from SRC.Custom_Exceptions.Custom_Error import EmptyEditerror
class USPhoneNumber(PhoneNumber):
    default_region_code = "US"
    phone_format = "NATIONAL"
    supported_regions = ["US"]
class CustomerCreate(BaseModel):
    name: str = Field(min_length=1,max_length=50)
    number: USPhoneNumber
    email: EmailStr
    timewith: int = Field(ge=0)
    model_config = ConfigDict(from_attributes=True)
class Customer_ID(BaseModel):
    customer_id : UUID4
    model_config = ConfigDict(from_attributes=True)

class Product_ID(BaseModel):
    product_id : UUID4
    model_config = ConfigDict(from_attributes=True)


class CustomerUpdate(BaseModel):
    name: str | None = Field(default=None,min_length=1,max_length=50)
    number: USPhoneNumber | None = None
    email: EmailStr | None = None
    timewith: int | None = Field(ge=0,le=100,default=None)
    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="after")
    def checkifempty(self):
        if not self.model_dump(exclude_none=True).values():
            raise EmptyEditerror("No edits were made please enter a edit to Customer and try again")
        return self
class ProductCreate(BaseModel):
    upc: str = Field(min_length=12,max_length=12,pattern=r"^[0-9]{12}$")
    name: str = Field(min_length=1,max_length=80)
    quantity: int = Field(ge=0,le=10000)
    price: int = Field(ge=0,le=10000)
    description: str = Field(max_length=99)
    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    upc: str | None = Field(default= None,min_length=12,max_length=12,pattern=r"^[0-9]{12}$")
    name: str | None = Field(default=None,min_length=1,max_length=80)
    quantity: int | None = Field(ge=0,le=10000,default=None)
    price: int | None = Field(ge=0,le=10000,default=None)
    description: str | None = Field(default=None,max_length=99)
    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="after")
    def checkifempty(self):
        if not self.model_dump(exclude_none=True).values():
            raise EmptyEditerror("No edits were made please enter a edit to Product and try again")
        return self