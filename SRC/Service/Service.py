import uuid

from SRC.Repo.Repository import Repository


class Service():
    def __init__(self,repository : Repository ):
        #super().__init__(db_path)
        self.repo = repository
#lookup methods are only for name currently must add different types of lookups
    def Lookup_product(self,name : str):
        if type(name) == str:
            products = self.repo.Search_product(name)
        else:
            raise TypeError(f"Only named lookup input must be String. Current input:{type(name)}")

        return products

    def Lookup_customer(self,name):
        if type(name) == str:
            customers = self.repo.Search_customer(name)
        else:
            raise TypeError(f"Named lookup only input must be String. Current input:{type(name)}")

        return customers
    def Add_item(self,upc : int,name : str,quantity : int,price : int,description : str):
        approved = { upc : int,name : str,quantity : int,price : int,description : str}
        for arg,types in approved.items():
            if type(arg) == types:
                continue
            else:
                raise TypeError(f"Input {arg} is the wrong type")
        self.repo.Add_product(upc,name,quantity,price,description)
    def Add_customer(self,name,number,email,timewith):
        approved = {name : str, number : str, email : str , timewith : int}
        for arg,types in approved.items():
            if type(arg) == types:
                continue
            else:
                raise TypeError(f"Input {arg} is the wrong type")
        self.repo.Add_customer_info(name,number,email,timewith)

    def Delete_item(self,product_id : str):
        if type(product_id) == str:
            self.repo.Delete_product_info(product_id=uuid.UUID(product_id))
        else:
            raise TypeError("Product_id is wrong type must be a String")

    def Delete_customer(self,customer_id: str):
        if type(customer_id) == str:
            self.repo.Delete_customer_info(customer_id=uuid.UUID(customer_id))
        else:
            raise TypeError("customer_id is wrong type must be a String")
    def Edit_item_info(self,item_id,upc = None,name = None,quantity = None,price = None,description = None):
        update_check = {"upc": upc, "name": name, "quantity": quantity, "price": price, "description": description}
        confirmed_updates = {}
        item_iduuid = uuid.UUID(item_id)
        for key, value in update_check.items():
            if value is not None:
                confirmed_updates[key] = value
        self.repo.Edit_product_info(item_iduuid,confirmed_updates)
    def Edit_customer_info(self,customer_id: str , name = None, number = None, email = None, timewith = None):
        update_check = {"name": name, "number": number, "email": email, "timewith": timewith}
        confirmed_updates = {}
        customer_iduuid =uuid.UUID(customer_id)
        for key,value in update_check.items():
            if value is not None:
                confirmed_updates[key] = value

        self.repo.Edit_customer_info(customer_iduuid,confirmed_updates)








