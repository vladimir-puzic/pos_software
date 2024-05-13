import time
import sqlite3
from people import create_employee, create_customer
from transactions import create_transaction
from datetime import date, datetime
from random import choice, randint

class DatabaseSession:
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.connection = None

#DATABASE MANAGEMENT

    def connect_to_database(self):
        self.connection = sqlite3.connect(f'{self._db_name}.db')

    def list_tables(self):
        cursor = self.connection.cursor()
        table_list = cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table';").fetchall()
        for table in table_list:
            print(table)
            print()

    def db_create_employees_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Employees ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'phone_number' INTEGER, 'employee_id' TEXT)")
    
    def db_create_customers_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Customers ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'date_of_birth' DATE, 'customer_id' INTEGER)")
   
    def db_create_items_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Items ('plu' INTAGER, 'name' TEXT, 'type' TEXT, 'weight' FLOAT, 'price' FLOAT)")

    def db_create_transactions_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Transactions ('transaction_id' TEXT, 'customer_id' INTAGER, 'employee_id' TEXT, 'total' FLOAT, 'timestamp' DATETIME)")
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Itemizer ('transaction_id' TEXT, 'plu' INTAGER, 'item_name' TEXT, 'amount' INTAGER)")

    def db_drop_table(self, table_name: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

#EMPLOYEE MANAGEMENT

    def db_create_employee(self, f_name: str, l_name: str, gender: str, phone_no: int, employee_id: str):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Employees VALUES ('{f_name}', '{l_name}', '{gender}', '{phone_no}', '{employee_id}')")
        self.connection.commit()

    def db_list_employees(self):
        cursor = self.connection.cursor()
        employees_list = cursor.execute(f"SELECT * FROM Employees").fetchall()
        for employee in employees_list:
            print(employee)
    
    def db_list_employee_id(self):
        cursor = self.connection.cursor()
        employee_id_list = cursor.execute(f"SELECT employee_id FROM Employees").fetchall()
        return employee_id_list
    
    def db_delete_employee_id(self, employee_id: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Employees WHERE employee_id = '{employee_id}'")
        self.connection.commit()    

    def db_delete_employee_all(self):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Employees")
        self.connection.commit()       

#CUSTOMER MANAGEMENT

    def db_create_customer(self, f_name: str, l_name: str, gender: str, dob: date, customer_id: int):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Customers VALUES ('{f_name}', '{l_name}', '{gender}', '{dob}', '{customer_id}')")
        self.connection.commit()

    def db_list_customers(self):
        cursor = self.connection.cursor()
        customers_list = cursor.execute(f"SELECT * FROM Customers").fetchall()
        for customer in customers_list:
            print(customer)

    def db_list_customer_id(self):
        cursor = self.connection.cursor()
        customer_id_list = cursor.execute(f"SELECT customer_id FROM Customers").fetchall()
        return customer_id_list
    
    def db_delete_customer_id(self, customer_id: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Customers WHERE customer_id = '{customer_id}'")
        self.connection.commit()    

    def db_delete_customer_all(self):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Customers")
        self.connection.commit()

#ITEM MANAGEMENT

    def db_create_item(self, plu: int, name: str, type: str, weight: float, price: float):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Items VALUES ('{plu}', '{name}', '{type}', '{weight}', '{price}')")
        self.connection.commit()
    
    def db_list_items(self):
        cursor = self.connection.cursor()
        items_list = cursor.execute(f"SELECT * FROM Items").fetchall()
        for item in items_list:
            print(item)
    
    def db_return_items(self):
        cursor = self.connection.cursor()
        items_list = cursor.execute(f"SELECT * FROM Items").fetchall()
        return items_list
    
    def db_list_item_plu(self):
        cursor = self.connection.cursor()
        item_plu_list = cursor.execute(f"SELECT plu FROM Items").fetchall()
        return item_plu_list
    
    def db_fetch_item_data(self, item_name):
        cursor = self.connection.cursor()
        item_data = cursor.execute(f"SELECT * FROM Items WHERE name='{item_name}'").fetchall()
        return item_data
    
    def db_delete_item_name(self, name: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Items WHERE name = '{name}'")
        self.connection.commit() 

    def db_delete_item_all(self):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Items")
        self.connection.commit()

#TRANSACTION MANAGEMENT

    def db_create_transaction(self, transaction_id: str, customer_id: str, employee_id: str, total: float, timestamp: datetime):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Transactions VALUES ('{transaction_id}', '{customer_id}', '{employee_id}', '{total}', '{timestamp}')")
        self.connection.commit()

    def db_itemize_transaction(self, transaction_id: str, plu, item_to_add: str, amount):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Itemizer VALUES ('{transaction_id}', '{plu}', '{item_to_add}', '{amount}')")
        self.connection.commit()

    def db_list_transactions(self):
        cursor = self.connection.cursor()
        transactions_list = cursor.execute(f"SELECT * FROM Transactions").fetchall()
        for transaction in transactions_list:
            print(transaction)
    
    def db_delete_transaction_id(self, transaction_id: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Transactions WHERE transaction_id = '{transaction_id}'")
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Itemizer WHERE transaction_id = '{transaction_id}'")
        self.connection.commit() 

    def db_delete_transactions_all(self):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Transactions")
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Itemizer")
        self.connection.commit()

def random_transaction():
    transaction_id, customer_id, employee_id, total, timestamp = create_transaction(session.db_list_customer_id(), session.db_list_employee_id(), 5.00)
    print(transaction_id, customer_id, employee_id, total, timestamp)
    session.db_create_transaction(transaction_id, customer_id, employee_id, total, timestamp)
    print(f'Transaction {transaction_id} created')
    list_of_items = session.db_return_items()
    choosen_items = randint(1, (len(list_of_items)))
    for item in range(choosen_items):
        item_data = choice(list_of_items)
        amount = randint(1, 10)
        session.db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount)

if __name__ == '__main__':
    db_name = input('db name:')
    session = DatabaseSession(db_name)
    session.connect_to_database()
    while True:
        wait_time = randint(2, 20)
        time.sleep(wait_time)
        random_transaction()
        print(f'{datetime.now()} Transaction created')