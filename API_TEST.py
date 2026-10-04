from fastapi import FastAPI,Depends,HTTPException
from database import Database
from Repository import Repository
from Service import Service
from typing import Annotated,Any
db = Database("superb.db")
repo = Repository(db)
serv = Service(repo)

app = FastAPI()


@app.on_event("startup")
def data(db_path,db : Annotated[Database,Depends(Database)]):

