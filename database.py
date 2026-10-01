import sqlite3
import databaseconfig
import PySide6
from PySide6.QtWidgets import QLabel, QLineEdit
from Scanning_data import scanner_reader
from contextlib import contextmanager

class Database():

    def __init__(self,db_path):
        self.connection = sqlite3.connect(db_path,check_same_thread=False)

        self.cursor = self.connection.cursor()


        self.Create_Tables()
    def _Execute(self,query,parameters):
        self.cursor.execute(query,parameters)
        self.connection.commit()
    def _Fetchall(self,query,parameters = ()):
        self.cursor.execute(query,parameters)
        return self.cursor.fetchall()
    @contextmanager
    def Transactions(self):
        try:
            yield
            self.connection.commit()
        except:
            raise



    def Create_Tables(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Product(product_id TEXT PRIMARY KEY,
                                                                   upc TEXT,
                                                                   Name TEXT,
                                                                   Quantity INTEGER,
                                                                   Price INTEGER,
                                                                   Description TEXT)
        """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Customer_Info(customer_id TEXT PRIMARY KEY,
                                                                        Name TEXT,
                                                                        Number TEXT,
                                                                        Email TEXT,
                                                                        TimeWith REAL)
        
        """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Sales(transaction_id TEXT PRIMARY KEY,
                                                                customer_id TEXT NOT NULL,
                                                                time_started TEXT NOT NULL,
                                                                completed INTEGER NOT NULL,
                                                                FOREIGN KEY(customer_id) REFERENCES Customer_Info(customer_id))
                                                                
                                                                
        """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS itemsale(transaction_id TEXT NOT NULL,
                                                                   product_id TEXT NOT NULL,
                                                                   Quantity INTEGER NOT NULL,
                                                                   Price INTEGER NOT NULL,
                                                                   FOREIGN KEY(transaction_id) REFERENCES Sales(transaction_id)
                                                                   FOREIGN KEY(product_id) REFERENCES Product(product_id))
                                                                   
                                                                   
        
        """)


        self.connection.commit()









#IX = Database("superb.db")
#IX.Edit_customer_info(5165762675376,number="646-3546-5679")
#IX.Insert_Data("Product","upc,Name,Quantity",(996357,"dick",99))
#startup_table()