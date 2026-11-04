import uuid
from SRC.Database.database import validates,validate_email,EmailNotValidError
from SRC.Repo.Repository import Repository
from SRC.Transaction_manager.Transaction_manager import Transaction_manager

class Service():
    def __init__(self,repository : Repository,trans_manager : Transaction_manager):
        #super().__init__(db_path)
        self.repo = repository
        self.transaction = trans_manager
#lookup methods are only for name currently must add different types of lookups
    #using the sqlalchemy validator decorator to make a standard validator for email on database edits

    def Lookup_product(self,name : str):
        if type(name) == str:
            session = self.transaction.start_transaction()
            products = self.repo.Search_product(name,session)
        else:
            raise TypeError(f"Only named lookup input must be String. Current input:{type(name)}")
        #self.transaction.end_transaction(session)
        return products

    def Lookup_customer(self,name : str):
        if type(name) == str:
            session = self.transaction.start_transaction()
            customers = self.repo.Search_customer(name,session)
        else:
            raise TypeError(f"Named lookup only input must be String. Current input:{type(name)}")

        return customers
    def Add_item(self,upc : str,name : str,quantity : int,price : int,description : str):
        approved = { upc : str,name : str,quantity : int,price : int,description : str}
        conn = self.transaction.start_transaction()
        for arg,types in approved.items():
            if type(arg) == types:
                continue
            else:
                raise TypeError(f"Input {arg} is the wrong type")
        added_product = self.repo.Add_product(upc,name,quantity,price,description)
        self.transaction.confirm_orm_object(conn, added_product)
        self.transaction.end_transaction(conn)

    def Add_customer(self,name : str,number : str,email : str,timewith : int):
        approved = {name : str, number : str, email : str , timewith : int}
        conn = self.transaction.start_transaction()
        for arg,types in approved.items():
            if type(arg) == types:
                continue
            else:
                raise TypeError(f"Input {arg} is the wrong type")
        customer = self.repo.Add_customer_info(name,number,email,timewith)
        self.transaction.confirm_orm_object(conn,customer)
        self.transaction.end_transaction(conn)



    def Delete_item(self,product_id : str):
        if type(product_id) == str:
            conn = self.transaction.start_transaction()
            sql = self.repo.Delete_product_info(product_id=uuid.UUID(product_id))
            self.transaction.execute_orm_sql(conn,sql)
            self.transaction.end_transaction(conn)
        else:
            raise TypeError("Product_id is wrong type must be a String")


    def Delete_customer(self,customer_id: str):
        if type(customer_id) == str:
            conn = self.transaction.start_transaction()
            sql = self.repo.Delete_customer_info(customer_id=uuid.UUID(customer_id))
            self.transaction.execute_orm_sql(conn,sql)
            self.transaction.end_transaction(conn)
        else:
            raise TypeError("customer_id is wrong type must be a String")

    def Edit_item_info(self,item_id : str,upc = None,name = None,quantity = None,price = None,description = None):
        update_check = {"upc": upc, "name": name, "quantity": quantity, "price": price, "description": description}
        approved_types = {upc : str, name : str, quantity : int, price : int, description : str}
        confirmed_updates = {}
        if type(item_id) == str:
            item_iduuid = uuid.UUID(item_id)
        else:
            raise TypeError("item_id must be a string")


        for key, value in update_check.items():
            if value is not None:
                if type(value) != approved_types[value]:
                    raise TypeError("incorrect type for edited column")
                confirmed_updates[key] = value
            else:
                continue
        conn = self.transaction.start_transaction()
        self.repo.Edit_product_info(item_iduuid,confirmed_updates,conn)
        self.transaction.end_transaction(conn)
    def Edit_customer_info(self,customer_id: str , name = None, number = None, email = None, timewith = None):
        update_check = {"name": name, "number": number, "email": email, "timewith": timewith}
        approved_types = {name:str,number:str,email:str,timewith:int}
        confirmed_updates = {}
        if type(customer_id) == str:

            customer_iduuid =uuid.UUID(customer_id)
        else:
            raise TypeError("customer_id must be str")
        for key,value in update_check.items():
            if value is not None:
                if type(value) != approved_types[value]:
                    raise TypeError("incorrect type for edited column")
                confirmed_updates[key] = value
            else:
                continue
        conn = self.transaction.start_transaction()
        self.repo.Edit_customer_info(customer_iduuid,confirmed_updates,conn)
        self.transaction.end_transaction(conn)








