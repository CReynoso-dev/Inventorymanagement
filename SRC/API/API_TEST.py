from fastapi import FastAPI,Depends
from SRC.Database.database import Database
from SRC.Repo.Repository import Repository
from SRC.Service.Service import Service
from typing import Annotated

db = Database("superb.db")
repo = Repository(db)
serv = Service(repo)

app = FastAPI()


@app.get("startup")
def data(db_path,db : Annotated[Database,Depends(Database)]):

