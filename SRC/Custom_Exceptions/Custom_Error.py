
class OutofstockError(Exception):
    def __init__(self,message,item,Amountreq,currentstock):
        super().__init__(message)
        self.message = message
        self.Amountreg = Amountreq
        self.currentstock = currentstock
        self.item = item

    def __str__(self):
        return f"{self.message}: requested {self.Amountreg} of {self.item} only {self.currentstock}."

class InvalidOperationError(Exception):
    def __init__(self):
        pass


    def __str__(self):
        pass


class UnknownResourceError(Exception):
    def __init__(self,message):
        super().__init__(message)


    def __str__(self):
        pass


class ProductnotfoundError(Exception):
    def __init__(self,message,searched_input):
        super().__init__(message)
        self.message = message
        self.searched_input = searched_input

    def __str__(self):
        return f"{self.searched_input} was not recognized as a known product\n {self.message} "
class Invalididerror(Exception):
    def __init__(self,message,inputed_id,typeofid):
        super().__init__(message)
        self.message = message
        self.inputed_id = inputed_id
        self.typeofid = typeofid


    def __str__(self):
        return f"""{self.inputed_id} entered for {self.typeofid} ID correct formats are:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx or xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx {self.message}"""
class DeleteunknownproductError(Exception):
    def __init__(self,message,searched_input):
        super().__init__(message)
        self.message = message
        self.searched_input = searched_input

    def __str__(self):
        return f"UUID: {self.searched_input} was not recognized\n{self.message}."
class Deleteunknowncustomererror(Exception):
    def __init__(self,message,searched_input):
        super().__init__(message)
        self.message = message
        self.searched_input = searched_input

    def __str__(self):
        return f"UUID: {self.searched_input} was not recognized\n{self.message}."

class Editunknownproducterror(Exception):
    def __init__(self,message,searched_input):
        super().__init__(message)
        self.message = message
        self.searched_input = searched_input

    def __str__(self):
        return f"UUID: {self.searched_input} was not recognized\n{self.message}."

class Editunknowncustomererror(Exception):
    def __init__(self,message,searched_input):
        super().__init__(message)
        self.message = message
        self.searched_input = searched_input

    def __str__(self):
        return f"UUID: {self.searched_input} was not recognized\n{self.message}."


class Incorrectcustomeremailformaterror(Exception):
    def __init__(self, message,emailinputed):
        super().__init__(message)
        self.message = message
        self.emailinputed = emailinputed
    def __str__(self):
        return f"incorrect email format submitted: {self.emailinputed} {self.message}"

class Incorrectcustomernumberlengtherror(Exception):
    def __init__(self,message,numberinputed):
        super().__init__(message)
        self.message = message
        self.numberinputed = numberinputed

    def __str__(self):
        return f"incorrect number format submitted: {self.numberinputed} {self.message}"
class Incorrectcustomernumbernxxformaterror(Exception):
    def __init__(self,message,numberinputed):
        super().__init__(message)
        self.message = message
        self.numberinputed = numberinputed


    def __str__(self):
        return f"incorrect number format submitted: {self.numberinputed} {self.message}"



class CustomernotfoundError(Exception):
    def __init__(self,message,searched_input):
        super().__init__(message)
        self.message = message
        self.searched_input = searched_input

    def __str__(self):
        return f"{self.searched_input} was not found in current customers \n {self.message}"


class TransactionnotcompletedError(Exception):
    def __init__(self,message,failed_transaction):
        super().__init__(message)
        self.message = message
        self.failed_transaction = failed_transaction


    def __str__(self):
        return f"{self.message} {self.failed_transaction} failed to complete rollback was initiated"


