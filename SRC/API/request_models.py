from pydantic import BaseModel,ConfigDict,AfterValidator,BeforeValidator,field_validator,Field
from SRC.Custom_Exceptions.Custom_Error import Incorrectcustomernumberlengtherror,Incorrectcustomernumbernxxformaterror
from pydantic_extra_types import phone_numbers


class CustomerCreate(BaseModel):
    name: str
    number: str = Field(min_length=10,max_length=10,pattern=r"^[0-9]+$")
    email: str
    timewith: int
    model_config = ConfigDict(from_attributes=True)
    @field_validator('number',mode= 'after')
    @classmethod
    def correctformatNumber(cls,enterednumber):
        # Unicode code points for '0' through '9'
        codes_0_to_9 = {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}

        # Unicode code points for '2' through '9'
        codes_2_to_9 = {50, 51, 52, 53, 54, 55, 56, 57}

        #checkforonlyint = all(digit in codes_0_to_9 or codes_2_to_9 for digit in enterednumber)


        if ord(enterednumber[0]) in codes_2_to_9 and ord(enterednumber[3]) in codes_2_to_9:
            return enterednumber
        else:
            raise Incorrectcustomernumbernxxformaterror("currently only supports US numbers this number is not valid",enterednumber)











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