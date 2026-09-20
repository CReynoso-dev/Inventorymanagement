import sqlite3
import databaseconfig
import PySide6
from PySide6.QtWidgets import QLabel, QLineEdit
from Scanning_data import scanner_reader



def delete_customer_data(CurrentDatabase,rowtodelete):
    pass
def add_customer_data(CurrentDatabase,text1):
    conn = sqlite3.connect(CurrentDatabase)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO customer_contact_info (customer_name,customer_number,customer_email) VALUES (?,?,?)",text1.split(","))
    conn.commit()
    return
def Search_function_cc(CurrentDatabase,Text_to_search):
    con = sqlite3.connect(CurrentDatabase)
    cursor = con.cursor()
    table = 'product'

    g = cursor.execute(f"SELECT name FROM pragma_table_info('{table}')")
    #g =cursor.execute(f"SELECT * FROM product WHERE customer_name LIKE '{Text_to_search}%' OR customer_number LIKE '{Text_to_search}%' OR customer_email LIKE '{Text_to_search}%';")
    data = g.fetchall()



    return print(data[:])
def default_storage():
    pass



def Creation_of_database(nod):
    con = sqlite3.connect(f"{nod}")
    cursor = con.cursor()

    cursor.execute("CREATE TABLE Product(id INTEGER PRIMARY KEY,Name,Quantity,Description")
    cursor.execute("CREATE TABLE Customer_data(Name,Number,Email,TimeWith)")
def Adding_product_upc(nod,upc):
    con = sqlite3.connect(f"{nod}")
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO product (id) VALUES(?)",(upc,),)
    con.commit()






def edit_table_insert(current_database):
    connection = sqlite3.connect(current_database)
    cursor = connection.cursor()
    n = cursor.execute("SELECT name FROM sqlite_master") # needs to add a option to choose a specific table to edit
    tablenames = n.fetchall()
    table = input(f"{tablenames} please choose a table to edit:")

    p = cursor.execute(f"PRAGMA table_info({table});")
    collumnsname = p.fetchall()


    #print(table)

    #print(collumnsname)

    value = "("
    for i in range(len(collumnsname)):
        value+="?,"
    value  = value.rstrip(",")
    value+=")"
    #print(value)
    data = input(f"please input data in this format {value}:")
    insert = f"INSERT INTO {table} VALUES{value}"
    print(data)
    cursor.execute(insert,(data.split(",")))
    connection.commit()

    
def edit_table_delete(current_database):
    connection = sqlite3.connect(current_database)
    cursor = connection.cursor()
    command = cursor.execute("SELECT name FROM sqlite_master")
    tablenames = command.fetchall()
    table_to_work_on = input(f"{tablenames} please choose one of these tables to edit:")
    command = cursor.execute(f"SELECT * FROM {table_to_work_on}")
    rows_raw_data = command.fetchall()
    refined_row_data = ""
    num = 0
    for row in rows_raw_data:
        #print(row)
        num += 1
        refined_row_data += f"{num}:{row}\n"
    row_to_delete = input(f"please choose a row to delete:\n{refined_row_data}")
    command = cursor.execute(f"DELETE FROM {table_to_work_on} WHERE rowid ={row_to_delete}")
    connection.commit()

def edit_table_edit(current_database):
    connection = sqlite3.connect(current_database)
    cursor = connection.cursor()
    command = cursor.execute("SELECT name FROM sqlite_master")
    tablenames = command.fetchall()
    table_to_edit = input(f"{tablenames} please choose a table to edit:")
    #command = cursor.execute(f"SELECT * FROM {table_to_edit}")
    #collumns_of_table = command.fetchall()
    menu = """ 
    1. rename TABLE 
    2. ADD COLUMN to TABLE
    3. DROP COLUMN from table
    4. rename COLUMN
    """
    menuchoice = input(f"TABLE being edited:{table_to_edit}{menu}\n please select a choice:")
    if menuchoice == "1":
        renamed_table = input(f"old table name:{table_to_edit}\nplease enter your new table name:")
        cursor.execute(f"ALTER TABLE {table_to_edit} RENAME TO {renamed_table};")
        connection.commit()
    elif menuchoice == "2":
        cn = cursor.execute(f"PRAGMA table_info({table_to_edit});")
        column_names = cn.fetchall()
        current_columns = ""
        for column in column_names:
            current_columns+= f"{column[1]},"
        current_columns = current_columns.rstrip(",")
        #print(current_columns)
        name_of_added_column = input(f"current columns are:{current_columns}\n please enter a new column to add:")
        command = cursor.execute(f"ALTER TABLE {table_to_edit} ADD COLUMN {name_of_added_column}")
        connection.commit()
    elif menuchoice == "3":
        cn = cursor.execute(f"PRAGMA table_info({table_to_edit});")
        column_names = cn.fetchall()
        current_columns = ""
        for column in column_names:
            current_columns+= f"{column[1]},"
        current_columns = current_columns.rstrip(",")
        column_to_delete = input(f"current columns are:{current_columns}\n please choose a column to delete:")
        command = cursor.execute(f"ALTER TABLE {table_to_edit} DROP COLUMN {column_to_delete}")
        connection.commit()
    elif menuchoice == "4":
        cn = cursor.execute(f"PRAGMA table_info({table_to_edit});")
        column_names = cn.fetchall()
        current_columns = ""
        for column in column_names:
            current_columns += f"{column[1]},"
        current_columns = current_columns.rstrip(",")
        column_to_rename = input(f"current columns are:{current_columns}\n please choose a column to rename:")
        new_name_of_column = input(f"you have chosen:{column_to_rename}\n please enter new name:")
        command = cursor.execute(f"ALTER TABLE {table_to_edit} RENAME {column_to_rename} TO {new_name_of_column}")
        connection.commit()


#edit_table_edit("inventoryonhand.db")
Search_function_cc("inventoryonhand.db","hey")
#scanner = scanner_reader()
#Adding_product_upc("inventoryonhand.db",scanner.start_reader(True))
#startup_table()