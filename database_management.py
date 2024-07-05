import sqlite3
from datetime import date, datetime

import session as s
#SESSION MANAGEMENT


def connect_to_database(db_name):
    s.s_connection = sqlite3.connect(f'{db_name}.db')
    s.s_cursor = s.s_connection.cursor()
    print(f"Connected to DB '{db_name}'")

def return_db_name(self):
    return self._db_name

def return_current_user(self):
    return self._user

#DATABASE MANAGEMENT

def db_list_tables():
    table_list = s.s_cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table';").fetchall()
    for table in table_list:
        print(table)
        print()

def db_create_users_table():
    s.s_cursor.execute("CREATE TABLE IF NOT EXISTS Users ('employee_id' TEXT, 'password' TEXT, 'access_level' INTEGER, UNIQUE(employee_id))")
    s.s_cursor.execute(f"INSERT OR IGNORE INTO Users VALUES ('vp123456', 'zyfoksvpsyeddagw', '3')")
    s.s_connection.commit()

def db_create_employees_table():
    s.s_cursor.execute("CREATE TABLE IF NOT EXISTS Employees ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'phone_number' INTEGER, 'employee_id' TEXT)")

def db_create_customers_table():
    s.s_cursor.execute("CREATE TABLE IF NOT EXISTS Customers ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'date_of_birth' DATE, 'customer_id' INTEGER)")

def db_create_items_table():
    s.s_cursor.execute("CREATE TABLE IF NOT EXISTS Items ('plu' INTAGER, 'name' TEXT, 'type' TEXT, 'weight' FLOAT, 'price' FLOAT)")

def db_create_transactions_table():
    s.s_cursor.execute("CREATE TABLE IF NOT EXISTS Transactions ('transaction_id' TEXT, 'customer_id' INTAGER, 'employee_id' TEXT, 'total' FLOAT, 'timestamp' DATETIME)")
    s.s_cursor.execute("CREATE TABLE IF NOT EXISTS Itemizer ('transaction_id' TEXT, 'plu' INTAGER, 'item_name' TEXT, 'amount' INTAGER)")

def db_drop_table(table_name: str):
    s.s_cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

#USER MANAGEMENT

def db_create_user(employee_id: str, password: str, access_level: int):
    s.s_cursor.execute(f"INSERT INTO Users VALUES ('{employee_id}', '{password}', '{access_level}')")
    s.s_connection.commit()

def db_check_user(employee_id: str):
    user_list = s.s_cursor.execute(f"SELECT employee_id FROM Users").fetchall()
    for index, item in enumerate(user_list):
        user_list[index] = item[0]

    if employee_id in user_list:
        return True
    return False

def db_check_password(pw_key: str, employee_id: str):
    db_key = s.s_cursor.execute(f"SELECT password FROM Users WHERE employee_id='{employee_id}'").fetchall()
    db_key = db_key[0][0]
    if db_key == pw_key:
        return True
    return False

#EMPLOYEE MANAGEMENT

def db_create_employee(f_name: str, l_name: str, gender: str, phone_no: int, employee_id: str):
    s.s_cursor.execute(f"INSERT INTO Employees VALUES ('{f_name}', '{l_name}', '{gender}', '{phone_no}', '{employee_id}')")
    s.s_connection.commit()

def db_list_employees():
    employees_list = s.s_cursor.execute(f"SELECT * FROM Employees").fetchall()
    for employee in employees_list:
        print(employee)

def db_list_employee_id():
    employee_id_list = s.s_cursor.execute(f"SELECT employee_id FROM Employees").fetchall()
    return employee_id_list

def db_delete_employee_id(employee_id: str):
    s.s_cursor.execute(f"DELETE FROM Employees WHERE employee_id = '{employee_id}'")
    s.s_connection.commit()    

def db_delete_employee_all():
    s.s_cursor.execute(f"DELETE FROM Employees")
    s.s_connection.commit()       

#CUSTOMER MANAGEMENT

def db_create_customer(f_name: str, l_name: str, gender: str, dob: date, customer_id: int):
    s.s_cursor.execute(f"INSERT INTO Customers VALUES ('{f_name}', '{l_name}', '{gender}', '{dob}', '{customer_id}')")
    s.s_connection.commit()

def db_list_customers():
    customers_list = s.s_cursor.execute(f"SELECT * FROM Customers").fetchall()
    for customer in customers_list:
        print(customer)

def db_list_customer_id():
    customer_id_list = s.s_cursor.execute(f"SELECT customer_id FROM Customers").fetchall()
    return customer_id_list

def db_delete_customer_id(customer_id: str):
    s.s_cursor.execute(f"DELETE FROM Customers WHERE customer_id = '{customer_id}'")
    s.s_connection.commit()    

def db_delete_customer_all():
    s.s_cursor.execute(f"DELETE FROM Customers")
    s.s_connection.commit()

#ITEM MANAGEMENT

def db_create_item(plu: int, name: str, type: str, weight: float, price: float):
    s.s_cursor.execute(f"INSERT INTO Items VALUES ('{plu}', '{name}', '{type}', '{weight}', '{price}')")
    s.s_connection.commit()

def db_list_items():
    items_list = s.s_cursor.execute(f"SELECT * FROM Items").fetchall()
    for item in items_list:
        print(item)

def db_return_items():
    items_list = s.s_cursor.execute(f"SELECT * FROM Items").fetchall()
    return items_list

def db_list_item_plu():
    item_plu_list = s.s_cursor.execute(f"SELECT plu FROM Items").fetchall()
    return item_plu_list

def db_fetch_item_data(item_name):
    item_data = s.s_cursor.execute(f"SELECT * FROM Items WHERE name='{item_name}'").fetchone()
    return item_data

def db_delete_item_name(name: str):
    s.s_cursor.execute(f"DELETE FROM Items WHERE name = '{name}'")
    s.s_connection.commit() 

def db_delete_item_all():
    s.s_cursor.execute(f"DELETE FROM Items")
    s.s_connection.commit()

#TRANSACTION MANAGEMENT

def db_create_transaction(transaction_id: str, customer_id: str, employee_id: str, total: float, timestamp: datetime):
    s.s_cursor.execute(f"INSERT INTO Transactions VALUES ('{transaction_id}', '{customer_id}', '{employee_id}', '{total}', '{timestamp}')")
    s.s_connection.commit()

def db_itemize_transaction(transaction_id: str, plu, item_to_add: str, amount):
    s.s_cursor.execute(f"INSERT INTO Itemizer VALUES ('{transaction_id}', '{plu}', '{item_to_add}', '{amount}')")
    s.s_connection.commit()

def db_list_transactions():
    transactions_list = s.s_cursor.execute(f"SELECT * FROM Transactions").fetchall()
    for transaction in transactions_list:
        print(transaction)

def db_delete_transaction_id(transaction_id: str):
    s.s_cursor.execute(f"DELETE FROM Transactions WHERE transaction_id = '{transaction_id}'")
    s.s_cursor.execute(f"DELETE FROM Itemizer WHERE transaction_id = '{transaction_id}'")
    s.s_connection.commit() 

def db_delete_transactions_all():
    s.s_cursor.execute(f"DELETE FROM Transactions")
    s.s_cursor.execute(f"DELETE FROM Itemizer")
    s.s_connection.commit()