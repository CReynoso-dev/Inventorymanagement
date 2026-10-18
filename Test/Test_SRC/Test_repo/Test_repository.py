from SRC.Repo.Repository import Repository
from SRC.Database.database import Database
from SRC.Service.Service import Service
import random
import string
db_test = Database("sqlite","testrepo")
repo = Repository(db_test)
serv = Service(repo)

def test_create_customer_info_success():

    name = 'customer_test_create' + "".join(random.choices(string.ascii_letters,k=9))
    number = "347" + "".join(random.choices(string.digits, k=7))
    email = "".join(random.choices(string.ascii_letters + string.ascii_uppercase)) + "@gmail.com"
    timewith = random.randint(1, 99)
    repo.Add_customer_info(name=name,number=number,email=email,timewith=timewith)
    createdrow = repo.Search_customer(name)
    assert createdrow[0][1] == name


def test_create_product_info_success():
    upc = ''.join(random.choices(string.digits, k=12))
    name = "product_test_create" + ''.join(random.choices(string.ascii_letters,k=9))
    quantity = random.randint(1,99)
    price = random.randint(1,1000)
    description = "THIS DESCRIPTION WAS WRITTEN EXCLUSIVLY BY CHATGPT:white cup"
    repo.Add_product(upc=upc,name=name,quantity=quantity,price=price,description=description)
    createdrow = repo.Search_product(name)
    assert createdrow[0][2] == name



def test_Delete_customer_info_success():
    name = 'customer_test_delete' + "".join(random.choices(string.ascii_letters,k=9))
    number = "347" + "".join(random.choices(string.digits, k=7))
    email = "".join(random.choices(string.ascii_letters + string.ascii_uppercase)) + "@gmail.com"
    timewith = random.randint(1, 99)
    repo.Add_customer_info(name=name,number=number,email = email,timewith=timewith)
    results = repo.Search_customer(name)
    customer_id = results[0][0]
    name = results[0][1]



    repo.Delete_customer_info(customer_id)

    assert len(repo.Search_customer(name)) == 0




def test_Delete_product_info_success():
    upc = ''.join(random.choices(string.digits, k=12))
    name = "product_test_delete" + ''.join(random.choices(string.ascii_letters, k=9))
    quantity = random.randint(1, 99)
    price = random.randint(1, 1000)
    description = "test description: test test test"
    repo.Add_product(upc=upc,name=name,quantity=quantity,price=price,description=description)
    results = repo.Search_product(name)
    product_id = results[0][0]
    name = results[0][2]
    repo.Delete_product_info(product_id)
    assert len(repo.Search_product(name)) == 0
#still have to finish creating test for edits
def test_Edit_customer_info_success():
    name = 'customer_test_before_edit' + "".join(random.choices(string.ascii_letters, k=9))
    number = "347" + "".join(random.choices(string.digits, k=7))
    email = "".join(random.choices(string.ascii_letters + string.ascii_uppercase)) + "@gmail.com"
    timewith = random.randint(1, 99)
    repo.Add_customer_info(name=name, number=number, email=email, timewith=timewith)
    results = repo.Search_customer(name)
    edited_name = "test_after_edit" + "".join(random.choices(string.ascii_letters,k=9))
    repo.Edit_customer_info(customer_id=results[0][0],confirmed_updates={"name":f"{edited_name}"})
    edited_results = repo.Search_customer(edited_name)
    assert edited_results[0][1] == edited_name


def test_Edit_product_info_success():
    upc = ''.join(random.choices(string.digits, k=12))
    name = "product_test_before_edit" + ''.join(random.choices(string.ascii_letters, k=9))
    quantity = random.randint(1, 99)
    price = random.randint(1, 1000)
    description = "test decription: test test test"
    repo.Add_product(upc=upc, name=name, quantity=quantity, price=price,
                     description=description)
    results = repo.Search_product(name)
    edited_name = "product_test_after_edit" + "".join(random.choices(string.ascii_letters,k=9))

    repo.Edit_product_info(product_id=results[0][0],confirmed_updates={"name":f"{edited_name}"})
    edited_results = repo.Search_product(edited_name)
    assert edited_results[0][2] == edited_name
