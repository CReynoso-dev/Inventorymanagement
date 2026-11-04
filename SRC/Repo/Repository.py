import uuid

from SRC.Database.database import Database
from sqlalchemy import select,delete
from SRC.Database.database import Customer,Product


class Repository():
    def __init__(self,db : Database):
        #super().__init__(db_path)
        self.db = db

    def Search_product(self, search,connection):



        product = connection.query(Product).filter(Product.name.like(f"{search}%")).all()

        return product






    def Search_customer(self, search,connection):
        customer = connection.query(Customer).filter(Customer.name.like(f"{search}%")).all()

        return customer

    def Add_product(self, upc, name, quantity,price, description):
            added_product = Product(upc = upc ,name = name ,quantity = quantity, price = price, description = description)
            return added_product




    def Add_customer_info(self, name, number, email, timewith):
        customer = Customer(name = name, number = number,email = email, timewith = timewith)
        return customer






    def Edit_customer_info(self, customer_id : uuid.UUID , confirmed_updates : dict,conn):

        customer = self.Get_Customer(customer_id,conn)
        for columns,data in confirmed_updates.items():
            setattr(customer,columns,data)



    def Get_product(self,product_id,conn):

        sql = select(Product).where(Product.product_id == product_id)
        product = conn.scalars(sql).one()
        return product
    def Get_Customer(self,customer_id,conn):
        sql = select(Customer).where(Customer.customer_id == customer_id)
        customer = conn.scalars(sql).one()
        return customer

    def Edit_product_info(self,product_id : uuid.UUID,confirmed_updates : dict,conn):


        product = self.Get_product(product_id,conn)

        for column, value in confirmed_updates.items():
            setattr(product,column,value)


    def Delete_product_info(self,product_id: uuid.UUID):
        sql = delete(Product).where(Product.product_id == product_id)
        return sql


    def Delete_customer_info(self,customer_id : uuid.UUID):
        sql = sql = delete(Customer).where(Customer.customer_id == customer_id)
        return sql














