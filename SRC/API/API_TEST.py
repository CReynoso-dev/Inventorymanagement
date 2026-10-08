from fastapi import FastAPI,Depends
from SRC.Database.database import Database
from SRC.Repo.Repository import Repository
from SRC.Service.Service import Service
from typing import Annotated


app = FastAPI()


@app.get("startup")
def data():
    pass

