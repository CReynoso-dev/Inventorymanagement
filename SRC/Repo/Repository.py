import uuid

from SRC.Database.database import Database
from sqlalchemy import select,delete,inspect
from sqlalchemy.orm import Session
from SRC.Database.database import Customer,Product


class Repository():
    def __init__(self,db : Database):
        #super().__init__(db_path)
        self.db = db

    def Search_product(self, search,connection : Session):



        product = connection.query(Product).filter(Product.name.like(f"{search}%")).all()


        return product






    def Search_customer(self, search,connection : Session):
        customer = connection.query(Customer).filter(Customer.name.like(f"{search}%")).all()

        return customer

    def Add_product(self, upc, name, quantity,price, description,session : Session):
            product = Product(upc = upc ,name = name ,quantity = quantity, price = price, description = description)
            session.add(product)
            return product




    def Add_customer_info(self, name, number, email, timewith,session : Session):
        customer = Customer(name = name, number = number,email = email, timewith = timewith)
        session.add(customer)
        return customer






    def Edit_customer_info(self, customer_id : uuid.UUID , confirmed_updates : dict,conn):

        customer = self._Get_Customer(customer_id, conn)
        for columns,data in confirmed_updates.items():
            setattr(customer,columns,data)



    def _Get_product(self, product_id, conn):

        sql = select(Product).where(Product.product_id == product_id)
        product = conn.scalars(sql).one()
        return product
    def _Get_Customer(self, customer_id, conn):
        sql = select(Customer).where(Customer.customer_id == customer_id)
        customer = conn.scalars(sql).one()
        return customer

    def Edit_product_info(self,product_id : uuid.UUID,confirmed_updates : dict,conn):


        product = self._Get_product(product_id, conn)

        for column, value in confirmed_updates.items():
            setattr(product,column,value)


    def Delete_product_info(self,product_id: uuid.UUID,session : Session):
        sql = delete(Product).where(Product.product_id == product_id)
        session.execute(sql)
        return sql


    def Delete_customer_info(self,customer_id : uuid.UUID,session : Session):
        sql = sql = delete(Customer).where(Customer.customer_id == customer_id)
        session.execute(sql)
        return sql














