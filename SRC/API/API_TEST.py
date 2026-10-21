from fastapi import FastAPI,Depends,Body,HTTPException
from SRC.Database.database import Database
from SRC.Repo.Repository import Repository
from SRC.Service.Service import Service
from typing import Annotated
from SRC.API.response_models import CustomerResponse,ProductResponse
from SRC.API.request_models import CustomerCreate,ProductCreate,CustomerUpdate,ProductUpdate

app = FastAPI()
def get_db(sql="sqlite",name="store.db"):
    return Database(sql=sql,db_name=name)

def get_repo(db=Depends(get_db)):
    return Repository(db)
def get_service(repo = Depends(get_repo)):
    return Service(repository=repo)


@app.post("/customer/")
def Add_customer(customer: CustomerCreate, service: Annotated[Service, Depends(get_service)]):
    #need to improve error catching
    try:
        service.Add_customer(name=customer.name,number=customer.number,email=customer.email,timewith=customer.timewith)
        return True
    except:
        raise HTTPException(400,"Invalid request to add customer")

@app.post("/item/",status_code=201)
def Add_item(item : ProductCreate, service: Annotated[Service, Depends(get_service)]):
    #need to improve error catching
    try:
        service.Add_item(upc=item.upc,name=item.name,quantity=item.quantity,price=item.price,description=item.description)
        return True
    except:
        raise HTTPException(400,"Invalid request to add item")
@app.get("/customer/{customer_name}", response_model=list[CustomerResponse])
def search_customer(customer_name: str,service : Annotated[Service,Depends(get_service)]):
    customers =service.Lookup_customer(customer_name)
    result = [CustomerResponse.model_validate(customer, from_attributes=True) for customer in customers]
    return result
@app.put("/customer/{customer_id}/edit")
def customer_update(customer_id : str,customer : CustomerUpdate,service : Annotated[Service,Depends(get_service)]):
    service.Edit_customer_info(customer_id,name=customer.name,number=customer.number,email=customer.email,timewith=customer.timewith)
    return customer

@app.get("/item/{item_name}", response_model=list[ProductResponse])
def item_data(item_name: str,service : Annotated[Service,Depends(get_service)]):
    items = service.Lookup_product(item_name)
    result = [ProductResponse.model_validate(product, from_attributes=True) for product in items]
    return result


@app.put("/item/{product_id}/edit")
def item_update(product_id : str,item : ProductUpdate,service : Annotated[Service,Depends(get_service)]):
    service.Edit_item_info(product_id,upc=item.upc,name=item.name,quantity=item.quantity,price=item.price,description=item.description)
    return item