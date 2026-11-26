
from SRC.Service.dto_models import ProductDTO,CustomerDTO
from SRC.Repo.Repository import Repository
from SRC.Transaction_manager.Transaction_manager import Transaction_manager
from SRC.Custom_Exceptions.Custom_Error import Deleteunknowncustomererror,Invalididerror,DeleteunknownproductError,OutofstockError,ProductnotfoundError,CustomernotfoundError
from SRC.API.request_models import Customer_ID,Product_ID,CustomerCreate,ProductCreate,CustomerUpdate,ProductUpdate
from SRC.API.response_models import CustomerResponse
from pydantic import UUID4
class Service():
    def __init__(self,repository : Repository,trans_manager : Transaction_manager):
        #super().__init__(db_path)
        self.repo = repository
        self.transaction = trans_manager
#lookup methods are only for name currently must add different types of lookups

    def Lookup_product(self,name : str):
        if type(name) == str:
            with self.transaction.start_transaction() as session:
                products = self.repo.Search_product(name,session)
                products_list = [ProductDTO.model_validate(product,from_attributes=True) for product in products]
                if len(products_list) > 0:
                    return products_list
                else:
                    raise ProductnotfoundError("Please ensure spelling is correct",name)
        else:
            raise TypeError(f"Only named lookup input must be String. Current input:{type(name)}")


    def Lookup_customer(self,name : str):
        if type(name) == str:
            with self.transaction.start_transaction() as session:
                customers = self.repo.Search_customer(name,session)
                customers_list = [CustomerDTO.model_validate(customer,from_attributes=True) for customer in customers]
                if len(customers_list) > 0:
                    return customers_list
                else:
                    raise CustomernotfoundError("please ensure spelling is correct",name)
        else:
            raise TypeError(f"Named lookup only input must be String. Current input:{type(name)}")

    def Add_item(self,upc : str,name : str,quantity : int,price : int,description :str):
        validated_item = ProductCreate(upc=upc,name=name,quantity=quantity,price=price,description=description)
        with self.transaction.start_transaction() as conn:
            self.repo.Add_product(validated_item.upc, validated_item.name, validated_item.quantity, validated_item.price, validated_item.description,conn)
            return validated_item


    def Add_customer(self,name : str,number : str,email : str,timewith : int):
        validated_customer = CustomerCreate(name=name,number=number,email=email,timewith=timewith)
        with self.transaction.start_transaction() as conn:
            self.repo.Add_customer_info(validated_customer.name, validated_customer.number, validated_customer.email, validated_customer.timewith,conn)
            return validated_customer





    def Delete_item(self, product_id : UUID4):
        validated_id = Product_ID(product_id = product_id)
        with self.transaction.start_transaction() as session:
            if (deletedrowsql := self.repo.Delete_product_info(product_id=validated_id.product_id,session= session)):
                deletedrow = [ProductDTO.model_validate(product,from_attributes=True) for product in deletedrowsql]
                return deletedrow
            else:
                raise DeleteunknownproductError("could not find product attached to UUID please confirm correct UUID and retry",product_id)



    def Delete_customer(self, customer_id: UUID4):
        validated_id = Customer_ID(customer_id = customer_id)
        with self.transaction.start_transaction() as session:
            if (deletedrowsql := self.repo.Delete_customer_info(customer_id=validated_id.customer_id,session= session)):# checks if row object is empty or not
                deletedrow = [CustomerDTO.model_validate(customer) for customer in deletedrowsql]
                return deletedrow
                #self.repo.Delete_customer_info(customer_id=uuid.UUID(customer_id),session= session)
            else:
                raise Deleteunknowncustomererror("enter customer id in one of the correct format listed",customer_id)

    def Edit_item_info(self,item_id : UUID4,upc = None,name = None,quantity = None,price = None,description = None):
        update_check = {"upc": upc, "name": name, "quantity": quantity, "price": price, "description": description}
        validated_id = Product_ID(product_id=item_id)
        validated_edits = ProductUpdate.model_validate(update_check).model_dump(exclude_none=True,exclude_unset =True)
        with self.transaction.start_transaction() as conn:
            self.repo.Edit_product_info(validated_id.product_id,validated_edits,conn)

    def Edit_customer_info(self,customer_id: UUID4 , name = None, number = None, email = None, timewith = None):
        update_check = {"name": name, "number": number, "email": email, "timewith": timewith}
        validated_id = Customer_ID(customer_id=customer_id)
        validated_edits = CustomerUpdate.model_validate(update_check).model_dump(exclude_none=True,exclude_unset= True)
        with self.transaction.start_transaction() as conn:
            self.repo.Edit_customer_info(validated_id.customer_id,validated_edits,conn)









