#file contains code for communicating with the database using SQLite

import sqlite3
from datetime import date, datetime

import session as s

#SQL STATEMENTS

def connect_to_database(db_name):
    s.s_connection = sqlite3.connect(f'{db_name}.db')
    s.s_cursor = s.s_connection.cursor()
    print(f"Connected to DB '{db_name}'")

def return_db_name(self): #can possibly be removed, as the db_name variable is now accessible from 'session' as 's_db_name'
    return self._db_name

def return_current_user(self): #same as for above
    return self._user

def query(query):
    data = s.s_cursor.execute(query).fetchall()
    return data

def query_single(query):
    data = s.s_cursor.execute(query).fetchone()
    return data

def statement(statement):
    s.s_cursor.execute(statement)

def commit():
    s.s_connection.commit()

#DATABASE MANAGEMENT

def db_list_tables():
    table_list = query(f"SELECT * FROM sqlite_master WHERE type='table';")
    for table in table_list:
        print(table)
        print()

def db_create_users_table():
    statement("CREATE TABLE IF NOT EXISTS Users ('employee_id' TEXT, 'password' TEXT, 'access_level' INTEGER, UNIQUE(employee_id))")
    statement(f"INSERT OR IGNORE INTO Users VALUES ('vp123456', 'zyfoksvpsyeddagw', '3')") #this employee account is created with the 'user.db'. It should be the first admin account used for further setup. The password 'hash' is hardcoded, this needs to be addressed
    commit()

def db_create_employees_table():
    statement("CREATE TABLE IF NOT EXISTS Employees ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'phone_number' INTEGER, 'employee_id' TEXT, 'email' TEXT)")

def db_create_customers_table():
    statement("CREATE TABLE IF NOT EXISTS Customers ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'date_of_birth' DATE, 'customer_id' INTEGER)")

def db_create_items_table():
    statement("CREATE TABLE IF NOT EXISTS Items ('plu' INTAGER, 'name' TEXT, 'type' TEXT, 'weight' FLOAT, 'price' FLOAT)")

def db_create_transactions_table():
    statement("CREATE TABLE IF NOT EXISTS Transactions ('transaction_id' TEXT, 'customer_id' INTAGER, 'employee_id' TEXT, 'total' FLOAT, 'timestamp' DATETIME)")
    statement("CREATE TABLE IF NOT EXISTS Itemizer ('transaction_id' TEXT, 'plu' INTAGER, 'item_name' TEXT, 'amount' INTAGER)")

def db_drop_table(table_name: str):
    statement(f"DROP TABLE IF EXISTS {table_name}")

#USER MANAGEMENT

def db_create_user(employee_id: str, password: str, access_level: int):
    statement(f"INSERT INTO Users VALUES ('{employee_id}', '{password}', '{access_level}')")
    commit()

def db_check_user(employee_id: str):
    user_list = query(f"SELECT employee_id FROM Users") # as per issue #22, using .fetchall() to gather data from DB is causing the output to be a list of tuples instead of a list of employee id's
    for index, item in enumerate(user_list):
        user_list[index] = item[0]

    if employee_id in user_list:
        return True
    return False

def db_check_password(pw_key: str, employee_id: str):
    db_key = query(f"SELECT password FROM Users WHERE employee_id='{employee_id}'")
    db_key = db_key[0][0]
    if db_key == pw_key:
        return True
    return False

#EMPLOYEE MANAGEMENT

def db_create_employee(f_name: str, l_name: str, gender: str, phone_no: int, employee_id: str, email: str):
    statement(f"INSERT INTO Employees VALUES ('{f_name}', '{l_name}', '{gender}', '{phone_no}', '{employee_id}', '{email}')")
    commit()

def db_list_employees():
    employees_list = query(f"SELECT * FROM Employees")
    for employee in employees_list:
        print(employee)

def db_list_employee_id():
    employee_id_list = query(f"SELECT employee_id FROM Employees")
    return employee_id_list

def db_delete_employee_id(employee_id: str):
    statement(f"DELETE FROM Employees WHERE employee_id = '{employee_id}'")
    commit()   

def db_delete_employee_all():
    statement(f"DELETE FROM Employees")
    commit()      

#CUSTOMER MANAGEMENT

def db_create_customer(f_name: str, l_name: str, gender: str, dob: date, customer_id: int):
    statement(f"INSERT INTO Customers VALUES ('{f_name}', '{l_name}', '{gender}', '{dob}', '{customer_id}')")
    commit()

def db_list_customers():
    customers_list = query(f"SELECT * FROM Customers")
    for customer in customers_list:
        print(customer)

def db_list_customer_id():
    customer_id_list = query(f"SELECT customer_id FROM Customers")
    return customer_id_list

def db_delete_customer_id(customer_id: str):
    statement(f"DELETE FROM Customers WHERE customer_id = '{customer_id}'")
    commit()   

def db_delete_customer_all():
    statement(f"DELETE FROM Customers")
    commit()

#ITEM MANAGEMENT

def db_create_item(plu: int, name: str, type: str, weight: float, price: float):
    statement(f"INSERT INTO Items VALUES ('{plu}', '{name}', '{type}', '{weight}', '{price}')")
    commit()

def db_list_items():
    items_list = query(f"SELECT * FROM Items")
    for item in items_list:
        print(item)

def db_return_items():
    items_list = query(f"SELECT * FROM Items")
    return items_list

def db_list_item_plu():
    item_plu_list = query(f"SELECT plu FROM Items")
    return item_plu_list

def db_fetch_item_data(item_name):
    item_data = query_single(f"SELECT * FROM Items WHERE name='{item_name}'")
    return item_data

def db_delete_item_name(name: str):
    statement(f"DELETE FROM Items WHERE name = '{name}'")
    commit()

def db_delete_item_all():
    statement(f"DELETE FROM Items")
    commit()

#TRANSACTION MANAGEMENT

def db_create_transaction(transaction_id: str, customer_id: str, employee_id: str, total: float, timestamp: datetime):
    statement(f"INSERT INTO Transactions VALUES ('{transaction_id}', '{customer_id}', '{employee_id}', '{total}', '{timestamp}')")
    commit()

def db_itemize_transaction(transaction_id: str, plu, item_to_add: str, amount):
    statement(f"INSERT INTO Itemizer VALUES ('{transaction_id}', '{plu}', '{item_to_add}', '{amount}')")
    commit()

def db_list_transactions():
    transactions_list = query(f"SELECT * FROM Transactions")
    for transaction in transactions_list:
        print(transaction)

def db_delete_transaction_id(transaction_id: str):
    statement(f"DELETE FROM Transactions WHERE transaction_id = '{transaction_id}'")
    statement(f"DELETE FROM Itemizer WHERE transaction_id = '{transaction_id}'")
    commit() 

def db_delete_transactions_all():
    statement(f"DELETE FROM Transactions")
    statement(f"DELETE FROM Itemizer")
    commit()