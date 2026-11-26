from fastapi.responses import JSONResponse
from fastapi import Request,FastAPI
from SRC.Custom_Exceptions.Custom_Error import Editunknownproducterror,Editunknowncustomererror,Incorrectcustomernumbernxxformaterror,Incorrectcustomernumberlengtherror,Incorrectcustomeremailformaterror,Deleteunknowncustomererror,Invalididerror,OutofstockError,DeleteunknownproductError,ProductnotfoundError,CustomernotfoundError

def Registerexceptionhandlers(app :FastAPI):
    app.add_exception_handler(Editunknownproducterror,Editunknownproducterrorhandler)
    app.add_exception_handler(Editunknowncustomererror,Editunknowncustomererrorhandler)
    app.add_exception_handler(CustomernotfoundError,Customernotfounderrorhandler)
    app.add_exception_handler(ProductnotfoundError,Productnotfounderrorhandler)
    app.add_exception_handler(Incorrectcustomernumberlengtherror,Incorrectnumberlengtherrorhandler)
    app.add_exception_handler(Incorrectcustomernumbernxxformaterror,Incorrectnumbernxxformaterrorhandler)
    app.add_exception_handler(Incorrectcustomeremailformaterror,Incorrectemailformaterrorhandler)
    app.add_exception_handler(OutofstockError,outofstockerrorhandler)
    app.add_exception_handler(DeleteunknownproductError,unknownproductdeleteerrorhandler)
    app.add_exception_handler(Deleteunknowncustomererror,unknowncustomerdeleteerrorhandler)
    app.add_exception_handler(Invalididerror,invalididerror)
def Editunknownproducterrorhandler(request : Request, exc : Editunknownproducterror):
    return JSONResponse(status_code=404,content={"detail":str(exc)})
def Editunknowncustomererrorhandler(request : Request, exc : Editunknowncustomererror):
    return JSONResponse(status_code=404,content={"detail":str(exc)})
def Productnotfounderrorhandler(request : Request, exc : ProductnotfoundError):
    return JSONResponse(status_code=404,content= {"detail":str(exc)})
def Customernotfounderrorhandler(request : Request, exc : CustomernotfoundError):
    return JSONResponse(status_code=404,content={"detail":str(exc)})
def Incorrectnumberlengtherrorhandler(request : Request, exc : Incorrectcustomernumberlengtherror):
    return JSONResponse(status_code=422,content={"detail":str(exc)})

def Incorrectnumbernxxformaterrorhandler(request : Request,exc : Incorrectcustomernumbernxxformaterror):
    return JSONResponse(status_code=422,content={"detail":str(exc)})


def Incorrectemailformaterrorhandler(request : Request,exc : Incorrectcustomeremailformaterror):
    return JSONResponse(status_code=422,content={"detail":str(exc)})

def outofstockerrorhandler(request : Request,exc: OutofstockError):
    return JSONResponse(status_code=422,content= {"detail":str(exc)})

def unknownproductdeleteerrorhandler(request : Request,exc : DeleteunknownproductError):
    return JSONResponse(status_code=404,content= {"detail":str(exc)})

def unknowncustomerdeleteerrorhandler(request : Request,exc : Deleteunknowncustomererror):
    return JSONResponse(status_code=404,content= {"detail":str(exc)})

def invalididerror(request : Request,exc : Invalididerror):
    return JSONResponse(status_code=400,content= {"detail":str(exc)})

