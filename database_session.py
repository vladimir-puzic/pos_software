import sqlite3
from datetime import date, datetime

class DatabaseSession:
    def __init__(self, db_name: str, user_id: str):
        self._db_name = db_name
        self.connection = None
        self.cursor = None
        self._user = user_id

#SESSION MANAGEMENT

    def connect_to_database(self):
        self.connection = sqlite3.connect(f'{self._db_name}.db')
        self.cursor = self.connection.cursor()
        log.write(f"{datetime.now()} [{self._user}] (connect_to_database) - Connected to DB '{self._db_name}\n")
        print(f"Connected to DB '{self._db_name}'")

    def return_db_name(self):
        return self._db_name

    def return_current_user(self):
        return self._user
    
#DATABASE MANAGEMENT

    def db_list_tables(self):
        table_list = self.cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table';").fetchall()
        for table in table_list:
            print(table)
            print()
        log.write(f"{datetime.now()} [{self._user}] (db_list_tables) - Listed existing tables\n")

    def db_create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Users ('employee_id' TEXT, 'password' TEXT, 'access_level' INTEGER)")
        log.write(f"{datetime.now()} (db_create_users_table) - Created 'Users' table\n")
        self.cursor.execute(f"INSERT INTO Users VALUES ('vp123456', '{generate_key('123456')}', '3')")
        self.connection.commit()
        log.write(f"{datetime.now()} (db_create_users_table) - Created admin user\n")

    def db_create_employees_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Employees ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'phone_number' INTEGER, 'employee_id' TEXT)")
        log.write(f"{datetime.now()} [{self._user}] (db_create_employees_table) - Created 'Employees' table\n")

    def db_create_customers_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Customers ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'date_of_birth' DATE, 'customer_id' INTEGER)")
        log.write(f"{datetime.now()} [{self._user}] (db_create_customers_table) - Created 'Customers' table\n")

    def db_create_items_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Items ('plu' INTAGER, 'name' TEXT, 'type' TEXT, 'weight' FLOAT, 'price' FLOAT)")
        log.write(f"{datetime.now()} [{self._user}] (db_create_items_table) - Created 'Items' table\n")

    def db_create_transactions_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Transactions ('transaction_id' TEXT, 'customer_id' INTAGER, 'employee_id' TEXT, 'total' FLOAT, 'timestamp' DATETIME)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Itemizer ('transaction_id' TEXT, 'plu' INTAGER, 'item_name' TEXT, 'amount' INTAGER)")
        log.write(f"{datetime.now()} [{self._user}] (db_create_transactions_table) - Created 'Transactions' and 'Itemizer' table\n")


    def db_drop_table(self, table_name: str):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        log.write(f"{datetime.now()} [{self._user}] (db_drop_table) - Dropped '{table_name}' table\n")

#USER MANAGEMENT

    def db_create_user(self, employee_id: str, password: str, access_level: int):
        self.cursor.execute(f"INSERT INTO Users VALUES ('{employee_id}', '{password}', '{access_level}')")
        self.connection.commit()

    def db_check_user(self, employee_id: str):
        user_list = self.cursor.execute(f"SELECT employee_id FROM Users").fetchall()
        for index, item in enumerate(user_list):
            user_list[index] = item[0]

        if employee_id in user_list:
            log.write(f'{datetime.now()} (db_check_user) - User check succeded for {employee_id}\n')
            return True
        log.write(f'{datetime.now()} (db_check_user) - User check failed for {employee_id}\n')
        return False

    def db_check_password(self, pw_key: str, employee_id: str):
        db_key = self.cursor.execute(f"SELECT password FROM Users WHERE employee_id='{employee_id}'").fetchall()
        db_key = db_key[0][0]
        if db_key == pw_key:
            log.write(f'{datetime.now()} (db_check_password) - Password check succeded\n')
            return True
        log.write(f'{datetime.now()} (db_check_password) - Password check failed\n')
        return False
    
#EMPLOYEE MANAGEMENT

    def db_create_employee(self, f_name: str, l_name: str, gender: str, phone_no: int, employee_id: str):
        self.cursor.execute(f"INSERT INTO Employees VALUES ('{f_name}', '{l_name}', '{gender}', '{phone_no}', '{employee_id}')")
        self.connection.commit()

    def db_list_employees(self):
        employees_list = self.cursor.execute(f"SELECT * FROM Employees").fetchall()
        for employee in employees_list:
            print(employee)
    
    def db_list_employee_id(self):
        employee_id_list = self.cursor.execute(f"SELECT employee_id FROM Employees").fetchall()
        return employee_id_list
    
    def db_delete_employee_id(self, employee_id: str):
        self.cursor.execute(f"DELETE FROM Employees WHERE employee_id = '{employee_id}'")
        self.connection.commit()    

    def db_delete_employee_all(self):
        self.cursor.execute(f"DELETE FROM Employees")
        self.connection.commit()       

#CUSTOMER MANAGEMENT

    def db_create_customer(self, f_name: str, l_name: str, gender: str, dob: date, customer_id: int):
        self.cursor.execute(f"INSERT INTO Customers VALUES ('{f_name}', '{l_name}', '{gender}', '{dob}', '{customer_id}')")
        self.connection.commit()

    def db_list_customers(self):
        customers_list = self.cursor.execute(f"SELECT * FROM Customers").fetchall()
        for customer in customers_list:
            print(customer)

    def db_list_customer_id(self):
        customer_id_list = self.cursor.execute(f"SELECT customer_id FROM Customers").fetchall()
        return customer_id_list
    
    def db_delete_customer_id(self, customer_id: str):
        self.cursor.execute(f"DELETE FROM Customers WHERE customer_id = '{customer_id}'")
        self.connection.commit()    

    def db_delete_customer_all(self):
        self.cursor.execute(f"DELETE FROM Customers")
        self.connection.commit()

#ITEM MANAGEMENT

    def db_create_item(self, plu: int, name: str, type: str, weight: float, price: float):
        self.cursor.execute(f"INSERT INTO Items VALUES ('{plu}', '{name}', '{type}', '{weight}', '{price}')")
        self.connection.commit()
    
    def db_list_items(self):
        items_list = self.cursor.execute(f"SELECT * FROM Items").fetchall()
        for item in items_list:
            print(item)
    
    def db_return_items(self):
        items_list = self.cursor.execute(f"SELECT * FROM Items").fetchall()
        return items_list
    
    def db_list_item_plu(self):
        item_plu_list = self.cursor.execute(f"SELECT plu FROM Items").fetchall()
        return item_plu_list
    
    def db_fetch_item_data(self, item_name):
        item_data = self.cursor.execute(f"SELECT * FROM Items WHERE name='{item_name}'").fetchone()
        return item_data
    
    def db_delete_item_name(self, name: str):
        self.cursor.execute(f"DELETE FROM Items WHERE name = '{name}'")
        self.connection.commit() 

    def db_delete_item_all(self):
        self.cursor.execute(f"DELETE FROM Items")
        self.connection.commit()

#TRANSACTION MANAGEMENT

    def db_create_transaction(self, transaction_id: str, customer_id: str, employee_id: str, total: float, timestamp: datetime):
        self.cursor.execute(f"INSERT INTO Transactions VALUES ('{transaction_id}', '{customer_id}', '{employee_id}', '{total}', '{timestamp}')")
        self.connection.commit()

    def db_itemize_transaction(self, transaction_id: str, plu, item_to_add: str, amount):
        self.cursor.execute(f"INSERT INTO Itemizer VALUES ('{transaction_id}', '{plu}', '{item_to_add}', '{amount}')")
        self.connection.commit()

    def db_list_transactions(self):
        transactions_list = self.cursor.execute(f"SELECT * FROM Transactions").fetchall()
        for transaction in transactions_list:
            print(transaction)
    
    def db_delete_transaction_id(self, transaction_id: str):
        self.cursor.execute(f"DELETE FROM Transactions WHERE transaction_id = '{transaction_id}'")
        self.cursor.execute(f"DELETE FROM Itemizer WHERE transaction_id = '{transaction_id}'")
        self.connection.commit() 

    def db_delete_transactions_all(self):
        self.cursor.execute(f"DELETE FROM Transactions")
        self.cursor.execute(f"DELETE FROM Itemizer")
        self.connection.commit()