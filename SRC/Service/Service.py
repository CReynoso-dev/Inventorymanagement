from SRC.Repo.Repository import Repository
class Service():
    def __init__(self,repository : Repository ):
        #super().__init__(db_path)
        self.repo = repository

    def Lookup_product(self,name):
        products = self.repo.Search_product(name)

        return products

    def Lookup_customer(self,name):
        customers = self.repo.Search_customer(name)

        return customers
    def Add_item(self,product_id : int,upc : int,name : str,quantity : int,price : int,description : str):
        approved = {product_id : int,upc : int,name : str,quantity : int,price : int,description : str}
        for arg,types in approved.items():
            if type(arg) == types:
                print(arg)
                continue
            else:
                raise TypeError(f"Input {arg} is the wrong type")
        print("you did it ")
        self.repo.Add_product(product_id,upc,name,quantity,price,description)
    def Delete_item(self,product_id : int):
        if type(product_id) == int:
            self.repo.Delete_product_info(product_id=product_id)
        else:
            raise TypeError("Product_id is wrong type must be int")
    def Edit_item_info(self):
        pass

