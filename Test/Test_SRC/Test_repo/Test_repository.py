from SRC.Repo.Repository import Repository
from SRC.Database.database import Database
from SRC.Service.Service import Service
import random
import string
db_test = Database("sqlite","/Users/fuckdouglass/Desktop/Inventorymanagement/Test/Test_SRC/Test_database/test.db")
repo = Repository(db_test)
serv = Service(repo)

def test_create_customer_info_success():
    randomname = 'H' + "".join(random.choices(string.ascii_letters + string.ascii_uppercase,k=9))
    repo.Add_customer_info(name=randomname,number="1234567890",email="test@gmail.com",timewith=50)
    createdrow = repo.Search_customer(randomname)
    assert createdrow[0][1] == randomname


def test_create_product_info_success():
    randomname = "H" + ''.join(random.choices(string.ascii_letters + string.ascii_uppercase,k=9))
    randomupc = ''.join(random.choices(string.digits,k=12))
    repo.Add_product(upc=randomupc,name=randomname,quantity=99,price=8,description="brown cups")
    createdrow = repo.Search_product(randomname)
    assert createdrow[0][2] == randomname



def test_Delete_customer_info_success():
    customer = repo.Search_customer('H')
    customer_id = customer[0][0]
    name = customer[0][2]



    repo.Delete_customer_info(customer_id)

    assert len(repo.Search_customer(name)) == 0




def test_Delete_product_info_success():
    product = repo.Search_product('H')
    product_id = product[0][0]
    name = product[0][2]
    repo.Delete_product_info(product_id)
    assert len(repo.Search_product(name)) == 0

def test_Edit_customer_info_success():
    search_result = repo.Search_customer("testdata")
    repo.Edit_customer_info(customer_id=search_result[0][0],confirmed_updates={"name":"testdata_edited"})

    repo.Edit_customer_info(customer_id=search_result[0][0],confirmed_updates={"name":"testdata"})

def test_Edit_product_info_success():
    search_result = repo.Search_product("cups")
    repo.Edit_product_info(product_id=search_result[0][0],confirmed_updates={"name":"cups_edited"})
    repo.Edit_product_info(product_id=search_result[0][0],confirmed_updates={"name":"cups"})