from database import Database

class Repository():
    def __init__(self,db):
        #super().__init__(db_path)
        self.db = db

    def Search_product(self, search):
        return self.db._Fetchall("""SELECT * FROM Product WHERE Name LIKE ?


        """, (search + "%",))

    def Search_customer(self, search):
        return self.db._Fetchall("""SELECT * FROM Customer_Info WHERE Name LIKE ?



        """, (search + "%",))

    def Add_product(self,product_id, upc, name, quantity,price, description):
        self.db.cursor.execute("""INSERT INTO Product VALUES (?,?,?,?,?,?)



        """, (product_id,upc, name, quantity, price, description))


    def Add_customer_info(self, customer_id, name, number, email, timewith):
        self.db.cursor.execute("""INSERT INTO Customer_Info VALUES (?,?,?,?,?)



        """, (customer_id, name, number, email, timewith))

    def Edit_customer_info(self, customer_id: str, name = None, number = None, email = None, timewith = None):
        update_check = {"Name": name, "Number": number, "Email": email, "TimeWith": timewith}
        confirmed_updates = {}
        u_query = ""
        u_paramaters = []
        for key, value in update_check.items():
            if value is not None:
                confirmed_updates[key] = value
        for column, value in confirmed_updates.items():
            u_query += f"{column} = ?,"

            u_paramaters.append(value)
        u_paramaters.append(customer_id)


        self.db.cursor.execute(f"""UPDATE Customer_Info 
        SET {u_query.rstrip(",")}
        WHERE customer_id = ?




        """, u_paramaters)
    def Edit_product_info(self,product_id,upc = None,name = None,quantity = None,description = None):
        update_check = {"upc":upc,"Name": name, "Quantity": quantity, "Description": description}
        confirmed_updates = {}
        u_query = ""
        u_paramaters = []
        for key, value in update_check.items():
            if value is not None:
                confirmed_updates[key] = value
        for column, value in confirmed_updates.items():
            u_query += f"{column} = ?,"

            u_paramaters.append(value)
        u_paramaters.append(product_id)


        self.db.cursor.execute(f"""UPDATE Product 
                SET {u_query.rstrip(",")}
                WHERE product_id = ?




                """, u_paramaters)
    def Delete_product_info(self,product_id: str):
        self.db.cursor.execute("""DELETE FROM Product
                      WHERE product_id = ?
                      
        
        
        
        """,(product_id,))

    def Delete_customer_info(self,customer_id: str):
        self.db.cursor.execute("""DELETE FROM Customer_info
                              WHERE customer_id = ?




                """, (customer_id,))
    def Add_sale(self,transaction_id,customer_id,time,completed):
        self.db.cursor.execute("""INSERT INTO Sales VALUES (?,?,?,?)""",(transaction_id,customer_id,time,completed))
    def Add_itemsale(self,transaction_id,product_id,quantity,price):
        self.db.cursor.execute("""INSERT INTO itemsale VALUES (?,?,?,?)""",(transaction_id,product_id,quantity,price))











#db = Database("superb.db")
#repo = Repository(db)

#repo.Delete_customer_info("209388292")
#repo.Edit_product_info(927383,name="pphead")
#print(repo.Search_customer("kimari"))