import sqlite3
import uuid
from typing import List
from contextlib import contextmanager
from sqlalchemy import create_engine,column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session,mapped_column,Mapped,validates,relationship
from email_validator import validate_email,EmailNotValidError

engine = create_engine("sqlite///store.db",connect_args={"check_same_thread":False})
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
base = declarative_base()

class Customer(base):
    __tablename__ = "Customer_info"
    customer_id : Mapped[uuid.uuid4()] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50))
    number : Mapped[str] = mapped_column(String(10))
    email : Mapped[str] = mapped_column(String(55))
    timewith : Mapped[int] = mapped_column(Integer)

    sales : Mapped[List["Sales"]] = relationship(back_populates="Sales")



    @validates("email")
    def Email_checker(self,key,address):
        if not address:
            raise ValueError("No email detected")
        try:
            email_info = validate_email(address,check_deliverability=False)

            return email_info.normalized
        except EmailNotValidError as error:
            print(f"Email invalid: {error}")
class Product(base):
    __tablename__ = "Product"
    product_id : Mapped[uuid.uuid4()] = mapped_column(primary_key=True)
    upc : Mapped[str] = mapped_column(String(12))
    name : Mapped[str] = mapped_column(String(80))
    quantity : Mapped[int] = mapped_column(Integer)
    price : Mapped[int] = mapped_column(Integer)
    description : Mapped[str] = mapped_column(String(99))

class Sales(base):
    __tablename__ = "Sales"
    transaction_id : Mapped[uuid.uuid4()] = mapped_column(primary_key=True)
    customer_id : Mapped[uuid.uuid4()] = mapped_column(ForeignKey("Customer_info.customer_id"))

    customer : Mapped["Customer"] = relationship(back_populates="Sales")
    itemsale : Mapped["Itemsale"] = relationship(back_populates="Sales")
class Itemsale(base):
    __tablename__ = "Itemsale"
    transaction_id : Mapped[uuid.uuid4()] = mapped_column(ForeignKey("Sales.transaction_id"))
    product_id : Mapped[uuid.uuid4()] = mapped_column(ForeignKey("Product.product_id"))
    quantity : Mapped[int] = mapped_column(Integer)
    price : Mapped[int] = mapped_column(Integer)

    sales : Mapped["Sales"] = relationship(back_populates="Itemsale")





#below is older pre orm database code


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