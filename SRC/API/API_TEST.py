from fastapi import FastAPI,Depends
from SRC.Database.database import Database
from SRC.Repo.Repository import Repository
from SRC.Service.Service import Service
from typing import Annotated
from SRC.API.request_models import Customer

app = FastAPI()
def get_db(sql="sqlite",name="store.db"):
    return Database(sql=sql,db_name=name)

def get_repo(db=Depends(get_db)):
    return Repository(db)
def get_service(repo = Depends(get_repo)):
    return Service(repository=repo)

@app.get("/customer/{customer_name}",response_model=Customer)
def customer_data(customer_name: str,service : Annotated[Service,Depends(get_service)]):
    customer =service.Lookup_customer(customer_name)
    return customer

