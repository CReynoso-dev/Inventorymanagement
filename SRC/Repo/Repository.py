import uuid

from SRC.Database.database import Database
from sqlalchemy import select,delete
from SRC.Database.database import Customer,Product


class Repository():
    def __init__(self,db : Database):
        #super().__init__(db_path)
        self.db = db

    def Search_product(self, search):
        with self.db.Get_connection() as conn:
            sql = select(Product).where(Product.name.in_([search]))
            result = []
            for product in conn.scalars(sql):
                result.append((product.product_id,product.upc,product.name,product.price,product.quantity,product.description))

        return result






    def Search_customer(self, search):
        with self.db.Get_connection() as conn:
            sql = select(Customer).where(Customer.name.in_([search]))
            result = []
            for customer in conn.scalars(sql):
                result.append((customer.customer_id, customer.name, customer.number, customer.email,
                               customer.timewith))

        return result

    def Add_product(self, upc, name, quantity,price, description):
        with self.db.Get_connection() as conn:
            name = Product(upc= upc ,name= name,quantity = quantity,price = price,description = description)
            conn.add(name)
            conn.commit()



    def Add_customer_info(self, name, number, email, timewith):
        with self.db.Get_connection() as conn:
            customer = Customer(name = name, number = number,email = email, timewith = timewith)
            conn.add(customer)
            conn.commit()






    def Edit_customer_info(self, customer_id:str, name = None, number = None, email = None, timewith = None):
        conn = self.db.Get_connection()
        sql = select(Customer).where(Customer.customer_id == uuid.UUID(customer_id))
        customer = conn.scalars(sql).one()

        update_check = {"name":name,"number":number,"email":email,"timewith":timewith}
        confirmed_updates = {}

        for key,value in update_check.items():
            if value is not None:
                confirmed_updates[key] = value
        print(confirmed_updates)
        for columns,data in confirmed_updates.items():
            setattr(customer,columns,data)

        conn.commit()


    def Edit_product_info(self,product_id : str,upc = None,name = None,quantity = None,description = None):
        conn = self.db.Get_connection()
        sql = select(Product).where(Product.product_id == uuid.UUID(product_id))
        product = conn.scalars(sql).one()
        update_check = {"upc":upc,"name": name, "quantity": quantity, "description": description}
        confirmed_updates = {}

        for key, value in update_check.items():
            if value is not None:
                confirmed_updates[key] = value
        for column, value in confirmed_updates.items():
            setattr(product,column,value)
        conn.commit()

    def Delete_product_info(self,product_id: str):
        conn = self.db.Get_connection()
        sql = delete(Product).where(Product.product_id == uuid.UUID(product_id))
        conn.execute(sql)
        conn.commit()

    def Delete_customer_info(self,customer_id : str):
        conn = self.db.Get_connection()
        sql = sql = delete(Customer).where(Customer.customer_id == uuid.UUID(customer_id))
        conn.execute(sql)
        conn.commit()













