import random
import string

from SRC.Service.Service import Service
from SRC.Database.database import Database
from SRC.Repo.Repository import Repository
import pytest
db = Database(db_name="servtest",sql="sqlite")
repo = Repository(db)
serv = Service(repo)

def test_add_item():
    upc = "".join(random.choices(string.digits,k=12))
    name = "testy_product" + "".join(random.choices(string.ascii_letters))
    quantity = random.randint(0,99)
    price = random.randint(0,1000)
    description = "THIS DESCRIPTION WAS WRITTEN EXCLUSIVLY BY CHATGPT:white cup"
    serv.Add_item(upc = upc,name= name,quantity=quantity,price= price,description=description)
    assert serv.Lookup_product(name)[0][2] == name





def test_add_customer():
    name = "mr.testymctesterson" + "".join(random.choices(string.ascii_letters ,k=11))
    number = "347" + "".join(random.choices(string.digits,k=7))
    email = "".join(random.choices(string.ascii_letters + string.ascii_uppercase)) + "@gmail.com"
    timewith = random.randint(1,99)
    serv.Add_customer(name = name,number = number,email = email,timewith = timewith)
    assert serv.Lookup_customer(name)[0][1] == name
def test_delete_item():
    upc = "".join(random.choices(string.digits, k=12))
    name = "testy_product_delete" + "".join(random.choices(string.ascii_letters))
    quantity = random.randint(0, 99)
    price = random.randint(0, 1000)
    description = "THIS DESCRIPTION WAS WRITTEN EXCLUSIVLY BY CHATGPT:white cup"
    serv.Add_item(upc,name,quantity,price,description)
    result = serv.Lookup_product(name)
    item_id_str = str(result[0][0])
    serv.Delete_item(item_id_str)
    assert len(serv.Lookup_product(name)) == 0
def test_delete_customer():
    name = "mr.test_delete" + "".join(random.choices(string.ascii_letters, k=11))
    number = "347" + "".join(random.choices(string.digits, k=7))
    email = "".join(random.choices(string.ascii_letters + string.ascii_uppercase)) + "@gmail.com"
    timewith = random.randint(1, 99)
    serv.Add_customer(name,number,email,timewith)
    result = serv.Lookup_customer(name)
    customer_id_str = str(result[0][0])
    serv.Delete_customer(customer_id_str)
    assert len(serv.Lookup_customer(name)) == 0
def test_edit_customer():
    name = "mr.test_before_edit" + "".join(random.choices(string.ascii_letters, k=11))
    number = "347" + "".join(random.choices(string.digits, k=7))
    email = "".join(random.choices(string.ascii_letters + string.ascii_uppercase)) + "@gmail.com"
    timewith = random.randint(1, 99)
    serv.Add_customer(name, number, email, timewith)
    result = serv.Lookup_customer(name)
    edited_name = "mr.test_after_edited" + "".join(random.choices(string.ascii_letters + string.ascii_uppercase))
    customer_id_str = str(result[0][0])
    serv.Edit_customer_info(customer_id=customer_id_str,name=edited_name,email="beenedited@gmail.com")
    edited_result =serv.Lookup_customer(name=edited_name)
    assert edited_result[0][1] == edited_name

def test_edit_item():
    upc = "".join(random.choices(string.digits, k=12))
    name = "testy_product_before_edit" + "".join(random.choices(string.ascii_letters))
    quantity = random.randint(0, 99)
    price = random.randint(0, 1000)
    description = "THIS DESCRIPTION WAS WRITTEN EXCLUSIVLY BY CHATGPT:white cup"
    serv.Add_item(upc, name, quantity, price, description)
    result = serv.Lookup_product(name)
    edited_name = "testy_product_after_edit" + "".join(random.choices(string.ascii_letters))
    item_id_str = str(result[0][0])
    serv.Edit_item_info(item_id=item_id_str,name=edited_name,description="YOU BEEN EDITED")
    edited_result = serv.Lookup_product(edited_name)
    assert edited_result[0][2] == edited_name
