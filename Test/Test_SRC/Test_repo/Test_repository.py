from SRC.Repo.Repository import Repository
from SRC.Database.database import Database
from SRC.Service.Service import Service

db_test = Database("sqlite","ABSOLUTE PATH HERE")
repo = Repository(db_test)
serv = Service(repo)
print(repo.Search_product("cups"))
repo.Delete_product_info("afd1f307-7a68-4095-b7e1-bd80a0f1614d")
#repo.Edit_product_info(product_id="afd1f307-7a68-4095-b7e1-bd80a0f1614d",quantity=67)