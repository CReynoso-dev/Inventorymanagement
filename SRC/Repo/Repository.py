import uuid

from SRC.Database.database import Database
from sqlalchemy import select,delete,inspect,update
from sqlalchemy.orm import Session
from SRC.Database.database import Customer,Product
from SRC.Custom_Exceptions.Custom_Error import Editunknownproducterror,Editunknowncustomererror,Deleteunknowncustomererror,ProductnotfoundError,CustomernotfoundError,DeleteunknownproductError
from SRC.API.request_models import Customer_ID,Product_ID,CustomerUpdate

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
            try:
                product = Product(upc = upc ,name = name ,quantity = quantity, price = price, description = description)
                session.add(product)
                return product
            except Exception as e:
                raise e




    def Add_customer_info(self, name, number, email, timewith,session : Session):
        try:
            customer = Customer(name = name, number = number,email = email, timewith = timewith)
            session.add(customer)
            return customer
        except Exception as e:
            raise e






    def Edit_customer_info(self, customer_id : uuid.UUID , confirmed_updates : dict,conn : Session):
        sqlUpdate = update(Customer).where(Customer.customer_id == customer_id).values(**confirmed_updates).returning(Customer.customer_id,Customer.name,Customer.number,Customer.email,Customer.timewith)

        if len((result := conn.execute(sqlUpdate).all())) > 0:
            return result
        else:
            raise Editunknowncustomererror("could not find customer attached to UUID please confirm correct UUID and retry",customer_id)


    def Edit_product_info(self,product_id : uuid.UUID,confirmed_updates : dict,conn : Session):
        sqlUpdate = update(Product).where(Product.product_id == product_id).values(**confirmed_updates).returning(Product.product_id,Product.upc,Product.name,Product.quantity,Product.price,Product.description)
        if len((result := conn.execute(sqlUpdate).all())) > 0:
            return result
        else:
            raise Editunknownproducterror("could not find product attached to UUID please confirm correct UUID and retry",product_id)


    def Delete_product_info(self, product_id: Product_ID, session : Session):
        sql = delete(Product).where(Product.product_id == product_id).returning(Product.product_id,Product.upc,Product.name,Product.quantity,Product.price,Product.description)

        if len((result := session.execute(sql).all())) > 0:
            return result
        else:
            raise DeleteunknownproductError("could not find product attached to UUID please confirm correct UUID and retry",product_id)


    def Delete_customer_info(self, customer_id : Customer_ID, session : Session):
        sql = delete(Customer).where(Customer.customer_id == customer_id).returning(Customer.customer_id,Customer.name,Customer.number,Customer.email,Customer.timewith)
        if len((result := session.execute(sql).all())) > 0:
            return result
        else:
            raise Deleteunknowncustomererror("could not find customer attached to UUID please confirm correct UUID and retry",customer_id)
















