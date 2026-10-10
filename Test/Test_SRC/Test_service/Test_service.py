from SRC.Service.Service import Service
from SRC.Database.database import Database
from SRC.Repo.Repository import Repository


db_test = Database(sql="sqlite",db_path="/Users/fuckdouglass/Desktop/Inventorymanagement/SRC/Database/store.db")
repo_test = Repository(db=db_test)
service_test = Service(repository=repo_test)

print(service_test.Lookup_product("mug"))
print(service_test.Lookup_customer("kimari"))
#service_test.Add_item(upc=63546345,name="mug",quantity=45,price=8,description="whitemug")
#service_test.Add_customer("christian","3478631934","reynosoc634@gmail.com",54)
#service_test.Edit_item_info(item_id = "f754de70-5b03-427b-839c-c52f5379060b",name="iggy",quantity=9)
#service_test.Edit_customer_info(customer_id="451d4f74-d77c-4595-8c1c-3e8378953ec1",name ="kimari",number ="3474375363",email ="youdidit@gmail.com",timewith=56)