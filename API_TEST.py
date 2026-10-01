from fastapi import FastAPI
from database import Database
from Repository import Repository
from Service import Service
db = Database("superb.db")
repo = Repository(db)
serv = Service(repo)

app = FastAPI()


@app.get("/")
def  root():
    with db.Transactions():
        results = serv.Lookup_product("cups")
    return results