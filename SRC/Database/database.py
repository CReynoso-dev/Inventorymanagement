import uuid
from typing import List,Optional
from contextlib import contextmanager
from sqlalchemy import create_engine,column,Integer,String,ForeignKey,text,Select
from sqlalchemy.orm import sessionmaker,Session,mapped_column,Mapped,validates,relationship,DeclarativeBase
from email_validator import validate_email,EmailNotValidError
from pathlib import Path

def new_uuid() -> uuid.UUID:
    # Note: Work around UUIDs with leading zeros: https://github.com/tiangolo/sqlmodel/issues/25
    # by making sure uuid str does not start with a leading 0
    val = uuid.uuid4()
    while val.hex[0] == '0':
        val = uuid.uuid4()
    return val
class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "Customer_info"
    customer_id : Mapped[uuid.UUID] = mapped_column(primary_key=True,default=new_uuid)
    name : Mapped[str] = mapped_column(String(50))
    number : Mapped[str] = mapped_column(String(10))
    email : Mapped[str] = mapped_column(String(55))
    timewith : Mapped[int] = mapped_column(Integer)

    sales : Mapped[List["Sales"]] = relationship(back_populates="customer")



    @validates("email")
    def Email_checker(self,key,address):
        if not address:
            raise ValueError("No email detected")
        try:
            email_info = validate_email(address,check_deliverability=False)

            return email_info.normalized
        except EmailNotValidError as error:
            return print(f"Email invalid: {error}")

class Product(Base):
    __tablename__ = "Product"
    product_id : Mapped[uuid.UUID] = mapped_column(primary_key=True,default=new_uuid)
    upc : Mapped[str] = mapped_column(String(12))
    name : Mapped[str] = mapped_column(String(80))
    quantity : Mapped[int] = mapped_column(Integer)
    price : Mapped[int] = mapped_column(Integer)
    description : Mapped[str] = mapped_column(String(99))

class Sales(Base):
    __tablename__ = "Sales"
    transaction_id : Mapped[uuid.UUID] = mapped_column(primary_key=True,default=new_uuid)
    customer_id : Mapped[uuid.UUID] = mapped_column(ForeignKey("Customer_info.customer_id"))

    customer : Mapped["Customer"] = relationship(back_populates="sales")
    #itemsale : Mapped["Itemsale"] = relationship(back_populates="sales")
#class Itemsale(Base): #recheck the use of this table might remake to be a line item
    #__tablename__ = "Itemsale"
    #transaction_id : Mapped[uuid.UUID] = mapped_column(ForeignKey("Sales.transaction_id"))
    #product_id : Mapped[uuid.UUID] = mapped_column(ForeignKey("Product.product_id"))
    #quantity : Mapped[int] = mapped_column(Integer)
    #price : Mapped[int] = mapped_column(Integer)

    #sales : Mapped["Sales"] = relationship(back_populates="itemsale")

#databaseurl = "sqlite:///store.db"
#engine = create_engine(databaseurl,connect_args={"check_same_thread":False})
#sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)



#below is older pre orm database code


class Database():
    def __init__(self,sql,db_path):

        self.sql = sql
        self.db_path = db_path
        self.db_url = f"{sql}:///{db_path}"

        self.engine = create_engine(self.db_url,connect_args={"check_same_thread":False})

        self.session = sessionmaker(autocommit=False,autoflush=False,bind=self.engine)

        #self.cursor = Session(self.engine)


        self.Create_Tables()


    def Create_Tables(self):
        Base.metadata.create_all(self.engine)

    def Get_connection(self):
        with Session(self.engine) as session:
            return session






#print(uuid.uuid4())
#IX = Database("sqlite","superb.db")
#IX.Edit_customer_info(5165762675376,number="646-3546-5679")
#IX.Insert_Data("Product","upc,Name,Quantity",(996357,"dick",99))
#startup_table()