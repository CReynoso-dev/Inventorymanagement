from fastapi import FastAPI,Depends
from SRC.Database.database import Database
from SRC.Repo.Repository import Repository
from SRC.Service.Service import Service
from typing import Annotated
from SRC.API.response_models import Customer,Product

app = FastAPI()
def get_db(sql="sqlite",name="store.db"):
    return Database(sql=sql,db_name=name)

def get_repo(db=Depends(get_db)):
    return Repository(db)
def get_service(repo = Depends(get_repo)):
    return Service(repository=repo)


@app.post("/customer/")
def Add_customer(customer: Customer,name : str,number : str,email : str,timewith : int, service: Annotated[Service, Depends(get_service)]):
    pass


@app.get("/customer/{customer_name}",response_model=Customer)
def customer_data(customer_name: str,service : Annotated[Service,Depends(get_service)]):
    customer =service.Lookup_customer(customer_name)
    return customer


@app.get("/item/{item_name}",response_model=Product)
def item_data(item_name: str,service : Annotated[Service,Depends(get_service)]):
    item = service.Lookup_product(item_name)
    return item



