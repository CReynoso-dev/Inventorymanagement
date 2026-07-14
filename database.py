import sqlite3
import databaseconfig




def access():
    database = databaseconfig.config()
    connection = sqlite3.connect(database)
    return connection

def startuptable():
    con = access()
    cursor = con.cursor()

    cursor.execute("CREATE TABLE Product(")

    

startuptable()