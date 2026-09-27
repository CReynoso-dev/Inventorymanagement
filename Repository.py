from database import Database

class Repository(Database):
    def __init__(self,db_path):
        super().__init__(db_path)


    def Search_product(self, search):
        return self._Fetchall("""SELECT * FROM Product WHERE Name LIKE ?


        """, (search + "%",))

    def Search_customer(self, search):
        return self._Fetchall("""SELECT * FROM Customer_Info WHERE Name LIKE ?



        """, (search + "%",))

    def Add_product(self, upc, name, quantity, description):
        self.connection.execute("""INSERT INTO Product VALUES (?,?,?,?)



        """, (upc, name, quantity, description))


    def Add_customer_info(self, customer_id, name, number, email, timewith):
        self.connection.execute("""INSERT INTO Customer_Info VALUES (?,?,?,?,?)



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


        self.connection.execute(f"""UPDATE Customer_Info 
        SET {u_query.rstrip(",")}
        WHERE customer_id = ?




        """, u_paramaters)
    def Edit_product_info(self,upc: str,name = None,quantity = None,description = None):
        update_check = {"Name": name, "Quantity": quantity, "Description": description}
        confirmed_updates = {}
        u_query = ""
        u_paramaters = []
        for key, value in update_check.items():
            if value is not None:
                confirmed_updates[key] = value
        for column, value in confirmed_updates.items():
            u_query += f"{column} = ?,"

            u_paramaters.append(value)
        u_paramaters.append(upc)


        self.connection.execute(f"""UPDATE Product 
                SET {u_query.rstrip(",")}
                WHERE upc = ?




                """, u_paramaters)
    def Delete_product_info(self,product_id: str):
        self.connection.execute("""DELETE FROM Product
                      WHERE product_id = ?
                      
        
        
        
        """,(product_id,))

    def Delete_customer_info(self,customer_id: str):
        self.connection.execute("""DELETE FROM Customer_info
                              WHERE customer_id = ?




                """, (customer_id,))





repo = Repository("superb.db")



print(repo.connection.in_transaction)


print(repo.connection.in_transaction)


#repo.Delete_customer_info("209388292")
#repo.Edit_product_info(927383,name="pphead")
#print(repo.Search_customer("kimari"))