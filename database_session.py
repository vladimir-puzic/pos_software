import sqlite3
from people import create_employee, create_customer
from transactions import create_transaction
from datetime import date, datetime
from random import choice, choices, randint, seed
from string import ascii_lowercase

class DatabaseSession:
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.connection = None
        self.cursor = None
        self._user = None

#SESSION MANAGEMENT

    def connect_to_database(self):
        self.connection = sqlite3.connect(f'{self._db_name}.db')
        self.cursor = self.connection.cursor()
        print(f"Connected to DB '{self._db_name}'")

    def return_db_name(self):
        return self._db_name

#DATABASE MANAGEMENT

    def db_list_tables(self):
        table_list = self.cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table';").fetchall()
        for table in table_list:
            print(table)
            print()

    def db_create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Users ('employee_id' TEXT, 'password' TEXT, 'access_level' INTEGER)")

    def db_create_employees_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Employees ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'phone_number' INTEGER, 'employee_id' TEXT)")
    
    def db_create_customers_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Customers ('first_name' TEXT, 'last_name' TEXT, 'gender' TEXT, 'date_of_birth' DATE, 'customer_id' INTEGER)")
   
    def db_create_items_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Items ('plu' INTAGER, 'name' TEXT, 'type' TEXT, 'weight' FLOAT, 'price' FLOAT)")

    def db_create_transactions_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Transactions ('transaction_id' TEXT, 'customer_id' INTAGER, 'employee_id' TEXT, 'total' FLOAT, 'timestamp' DATETIME)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Itemizer ('transaction_id' TEXT, 'plu' INTAGER, 'item_name' TEXT, 'amount' INTAGER)")


    def db_drop_table(self, table_name: str):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

#USER MANAGEMENT

    def db_create_user(self, employee_id: str, password: str, access_level: int):
        self.cursor.execute(f"INSERT INTO Users VALUES ('{employee_id}', '{password}', '{access_level}')")
        self.connection.commit()

    def db_check_user(self, employee_id: str):
        user_list = self.cursor.execute(f"SELECT employee_id FROM Users").fetchall()
        for index, item in enumerate(user_list):
            user_list[index] = item[0]

        if employee_id in user_list:
            return True
        return False

    def db_check_password(self, pw_key: str, employee_id: str):
        db_key = self.cursor.execute(f"SELECT password FROM Users WHERE employee_id='{employee_id}'").fetchall()
        db_key = db_key[0][0]
        if db_key == pw_key:
            return True
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



#MENU CLASS

class Menu:
    def __init__(self) -> None:
        self._header = ''
        self._options = {
            1: None, 
            2: None, 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: None
        }

    def __str__(self) -> str:
        return self._header
    
    def list_options(self):
        for option in self._options:
            if self._options[option] == None:
               continue
            print(f'{option} - {self._options[option]}')

    def choose_option(self):
        option = int(input(''))
        return self._options[option]

    def execute(self):
        global menu 
        global option
        menu = option

#Menu Item Class

class MenuItem:
    def __init__(self) -> None:
        self._header = ''
        self._function = None  

    def __str__(self):
        return self._header

    def execute(self):
        self._function()

#UTILITY FUNCTIONS

class MenuReturn(MenuItem):
    def __init__(self, return_menu: Menu) -> None:
        super().__init__()
        self._header = f'Return - ' + str(return_menu)
        self._menu = return_menu

    def execute(self):
        global menu 
        menu = self._menu()

#MAIN MENU

class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = f'{db_name} - Main Menu'
        self._options = {
            1: MenuTransactionManagement(), 
            2: MenuCustomerManagement(), 
            3: MenuEmployeeManagement(), 
            4: MenuItemManagement(), 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: MenuDatabaseManagement(),
            0: None
        }

#TRANSACTIONS

#TRANSACTION MANAGEMENT MENU

class MenuTransactionManagement(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Transaction Management'
        self._options = {
            1: ListTransactions(), 
            2: MenuCreateTransactions(), 
            3: MenuDeleteTransactions(), 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MainMenu)
        }

#CREATE TRANSACTIONS MENU

class MenuCreateTransactions(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Transactions'
        self._options = {
            1: CreateTransactionCustom(), 
            2: CreateTransactionRandom(), 
            3: CreateTransactionMultiple(), 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuTransactionManagement)
        }     

#DELETE TRANSACTIONS MENU

class MenuDeleteTransactions(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Transactions'
        self._options = {
            1: DeleteTransactionID(), 
            2: DeleteTransactionAll(), 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuTransactionManagement)
        }        

#Transaction Items

#List Transactions

class ListTransactions(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'List Transactions'
        self._function = session.db_list_transactions

    def execute(self):
        self._function()

#Create Transactions
    #Create Transaction Custom

class CreateTransactionCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Transaction'
        self._function = session.db_create_transaction
    
    def execute(self):
        transaction_id = input('Transaction ID: ')
        customer_id = int(input('Customer ID: '))
        employee_id = input('Employee ID: ')
        total = input('Total: ')
        timestamp = datetime.now()
        if timestamp == None:
            timestamp = datetime.now()
        self._function(transaction_id, customer_id, employee_id, total, timestamp)
        print(f'Transaction {transaction_id} created')

        while True:
            item_to_add = input('Select item: ')
            if item_to_add == '':
                break
            item_data = session.db_fetch_item_data(item_to_add)
            amount_to_add = int(input('Amount: '))
            for item in range(amount_to_add):
                print(transaction_id, item_data[0], item_data[1], amount_to_add)
                session.db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount_to_add)

    #Create Transaction Random

class CreateTransactionRandom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Random Transaction'
        self._function = session.db_create_transaction

    def execute(self):
        transaction_id, customer_id, employee_id, total, timestamp = create_transaction(session.db_list_customer_id(), session.db_list_employee_id(), 5.00)
        print(transaction_id, customer_id, employee_id, total, timestamp)
        self._function(transaction_id, customer_id, employee_id, total, timestamp)
        print(f'Transaction {transaction_id} created')
        list_of_items = session.db_return_items()
        choosen_items = randint(1, (len(list_of_items)))
        for item in range(choosen_items):
            item_data = choice(list_of_items)
            amount = randint(1, 10)
            session.db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount)

    #Create Transaction Multiple
    
class CreateTransactionMultiple(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Multiple Transactions'
        self._function = session.db_create_transaction

    def execute(self):
        transaction_number = int(input('Number of transactions: '))
        if transaction_number == 0:
            return
        for number in range(transaction_number):
            transaction_id, customer_id, employee_id, total, timestamp = create_transaction(session.db_list_customer_id(), session.db_list_employee_id(), 5.00)
            print(transaction_id, customer_id, employee_id, total, timestamp)
            self._function(transaction_id, customer_id, employee_id, total, timestamp)
            print(f'Transaction {transaction_id} created')
            list_of_items = session.db_return_items()
            choosen_items = randint(1, len(list_of_items))
            for item in range(choosen_items):
                item_data = choice(list_of_items)
                amount = randint(1, 10)
                session.db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount)

#Delete Transactions
    #Delete Transaction via ID

class DeleteTransactionID(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Transaction via ID'
        self._function = session.db_delete_transaction_id

    def execute(self):
        transaction_id_prompt = input('Enter Transaction ID: ')
        self._function(transaction_id_prompt)

    #Delete Transaction All

class DeleteTransactionAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Transactions'
        self._function = session.db_delete_transactions_all
    
    def execute(self):
        self._function()

#CUSTOMERS
        
#CUSTOMER MANAGEMENT MENU

class MenuCustomerManagement(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Customer Management'
        self._options = {
            1: ListCustomers(), 
            2: MenuCreateCustomer(), 
            3: MenuDeleteCustomer(), 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MainMenu)
        }

#CREATE CUSTOMERS MENU

class MenuCreateCustomer(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Customers'
        self._options = {
            1: CreateCustomerCustom(), 
            2: CreateCustomerRandom(), 
            3: CreateCustomerMultiple(), 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuCustomerManagement)
        }            

#DELETE CUSTOMERS MENU

class MenuDeleteCustomer(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Customers'
        self._options = {
            1: DeleteCustomerID(), 
            2: DeleteCustomerAll(), 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuCustomerManagement)
        }

#Customer Items

#List Customers

class ListCustomers(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'List Customers'
        self._function = session.db_list_customers
    
    def execute(self):
        self._function()

#Create Customers
    #Create Customer Custom

class CreateCustomerCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Customer'
        self._function = session.db_create_customer
    
    def execute(self):
        f_name = input('First name: ')
        l_name = input('Last name: ')
        gender = input('Gender: ')
        year = int(input('Year of birth: '))
        month = int(input('Month: '))
        day = int(input('Day: '))
        dob = date(year, month, day)
        customer_id = input('Customer ID:')
        self._function(f_name, l_name, gender, dob, customer_id)

    #Create Customer Random

class CreateCustomerRandom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Random Customer'
        self._function = session.db_create_customer
    
    def execute(self):
        f_name, l_name, gender, dob, customer_id = create_customer()
        print (f_name, l_name, gender, dob, customer_id)
        self._function(f_name, l_name, gender, dob, customer_id)

    #Create Customer Multiple

class CreateCustomerMultiple(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Multiple Customers'
        self._function = session.db_create_customer
    
    def execute(self):    
        customer_number = int(input('Number of customers: '))
        if customer_number == 0:
            return
        for number in range(customer_number):
            f_name, l_name, gender, dob, customer_id = create_customer()
            print (f_name, l_name, gender, dob, customer_id)
            self._function(f_name, l_name, gender, dob, customer_id)

#Delete Customers
    #Delete Customer via ID

class DeleteCustomerID(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Customer via ID'
        self._function = session.db_delete_customer_id

    def execute(self):
        customer_id_prompt = int(input('Enter Customer ID: '))
        self._function(customer_id_prompt)

    #Delete Customer All

class DeleteCustomerAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Customers'
        self._function = session.db_delete_customer_all
    
    def execute(self):
        self._function()

#EMPLOYEES

#EMPLOYEE MANAGEMENT MENU

class MenuEmployeeManagement(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Employee Management'
        self._options = {
            1: ListEmployees(), 
            2: MenuCreateEmployee(), 
            3: MenuDeleteEmployees(), 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MainMenu)
        }

#CREATE EMPLOYEES MENU

class MenuCreateEmployee(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Employees'
        self._options = {
            1: CreateEmployeeCustom(), 
            2: CreateEmployeeRandom(), 
            3: CreateEmployeeMultiple(), 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuEmployeeManagement)
        }

#DELETE EMPLOYEES MENU

class MenuDeleteEmployees(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Employees'
        self._options = {
            1: DeleteEmployeeID(), 
            2: DeleteEmployeeAll(), 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuEmployeeManagement)
        }

#Employee Items

#List Employees

class ListEmployees(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'List Employees'
        self._function = session.db_list_employees
    
    def execute(self):
        self._function()

#Create Employees
    #Create Employees Custom

class CreateEmployeeCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Employee'
        self._function = session.db_create_employee
    
    def execute(self):
        f_name = input('First name: ')
        l_name = input('Last name: ')
        gender = input('Gender: ')
        phone_no = int(input('Phone number: '))
        employee_id = input('Employee ID:')
        self._function(f_name, l_name, gender, phone_no, employee_id)

    #Create Employee Random

class CreateEmployeeRandom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Random Employe'
        self._function = session.db_create_employee
    
    def execute(self):
        f_name, l_name, gender, phone_no, employee_id = create_employee()
        print (f_name, l_name, gender, phone_no, employee_id)
        self._function(f_name, l_name, gender, phone_no, employee_id)  

    #Create Employee Multiple

class CreateEmployeeMultiple(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Multiple Employees'
        self._function = session.db_create_employee
    
    def execute(self):
        employee_number = int(input('Number of employees: '))
        if employee_number == 0:
            return
        for number in range(employee_number):
            f_name, l_name, gender, phone_no, employee_id = create_employee()
            print (f_name, l_name, gender, phone_no, employee_id)
            self._function(f_name, l_name, gender, phone_no, employee_id)        

#Delete Employees
    #Delete Employee via ID

class DeleteEmployeeID(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Employee via ID'
        self._function = session.db_delete_employee_id
    
    def execute(self):
        employee_id_prompt = input('Enter Employee ID: ')
        self._function(employee_id_prompt)        

    #Delete Employee All

class DeleteEmployeeAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Employees'
        self._function = session.db_delete_employee_all
    
    def execute(self):
        self._function()

#ITEMS

#ITEM MANAGEMENT MENU

class MenuItemManagement(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Item Management'
        self._options = {
            1: ListItems(), 
            2: MenuCreateItems(), 
            3: MenuDeleteItems(), 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MainMenu)
        }            

#CREATE ITEMS MENU

class MenuCreateItems(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Items'
        self._options = {
            1: CreateItemCustom(), 
            2: CreateItemStandardList(), 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuItemManagement)
        }   

#DELETE ITEMS MENU

class MenuDeleteItems(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Items'
        self._options = {
            1: DeleteItemName(), 
            2: DeleteItemAll(), 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuItemManagement)
        }    

#Item Items

#List Items

class ListItems(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'List Items'
        self._function = session.db_list_items
    
    def execute(self):
        self._function()

#Create Items
    #Create Custom Item

class CreateItemCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Item'
        self._function = session.db_create_item
    
    def execute(self):
        plu = int(input('Item PLU: '))
        name = input('Item name:')
        type = input('Type: ')
        weight = float(input('Weight: '))
        price = float(input('Price: '))
        self._function(plu, name, type, weight, price)        

    #Create Standard List Item

class CreateItemStandardList(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Standard List of Items'
        self._function = session.db_create_item
    
    def execute(self):
        milk = (644455, 'Milk', 'Dairy', 1, 2.50)
        eggs = (994111, 'Eggs', 'Dairy' , 0.5, 3.00)                           
        cheese = (222449, 'Cheese', 'Dairy', 1, 10.00)
        bread = (227779, 'Bread', 'Baked Goods', 0.5, 1.60)
        coffee = (222666, 'Coffee', 'Beverages', 0.5, 5.00)
        juice = (588444, 'Juice', 'Beverages', 1, 3.50)
        pork = (766611, 'Pork', 'Meat', 1, 13)
        chicken_breast = (222444, 'Chicken Breast', 'Meat', 1, 10)
        item_standard_list = [milk, eggs, cheese, bread, coffee, juice, pork, chicken_breast]
        for item in item_standard_list:
            plu, name, type, weight, price = item
            session.db_create_item(plu, name, type, weight, price)

#Delete Items
    #Delete Items via Name

class DeleteItemName(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Item via Name'
        self._function = session.db_delete_item_name
    
    def execute(self):
        item_name_prompt = input('Enter Item Name:')
        self._function(item_name_prompt)
        
    #Delete Items All

class DeleteItemAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Items'
        self._function = session.db_delete_item_all
    
    def execute(self):
        self._function()

#DATABASE MANAGEMENT MENU

class MenuDatabaseManagement(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Database Management'
        self._options = {
            1: MenuTableManagement(), 
            2: None, 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MainMenu)
        }

#TABLE MANAGEMENT MENU

class MenuTableManagement(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Table Management'
        self._options = {
            1: ListTables(), 
            2: MenuCreateTables(), 
            3: None, 
            4: None, 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuDatabaseManagement)
        }

#CREATE TABLES MENU

class MenuCreateTables(Menu):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Tables'
        self._options = {
            1: CreateTableTransactions(), 
            2: CreateTableCustomers(), 
            3: CreateTableEmployees(), 
            4: CreateTableItems(), 
            5: None, 
            6: None, 
            7: None, 
            8: None, 
            9: None,
            0: MenuReturn(MenuTableManagement)
        }

#List Tables

class ListTables(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'List Tables'
        self._function = session.db_list_tables

#Create Tables
    #Create Transactions Table

class CreateTableTransactions(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Transactions Table'
        self._function = session.db_create_transactions_table

    #Create Customers Table

class CreateTableCustomers(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Customers Table'
        self._function = session.db_create_customers_table

    #Create Employees Table

class CreateTableEmployees(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Employees Table'
        self._function = session.db_create_employees_table

    #Create Items Table

class CreateTableItems(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Items Table'
        self._function = session.db_create_items_table

#LOGIN
def login():
    session = DatabaseSession('users')
    session.connect_to_database()
    session.db_create_users_table()

    employee_id = input('Employee ID: ')
    password = input('Password: ')

    if session.db_check_user(employee_id) == False:
        create_user(employee_id, session)
        return
    
    pw_key = generate_key(password)
    auth = session.db_check_password(pw_key, employee_id)

    return auth

def generate_key(password):
    seed(password)
    char_list = choices(ascii_lowercase, k=16)
    pw_key = ''.join(char_list)

    return pw_key

def create_user(employee_id, session):
    print(f'Employee {employee_id} does not exist.')
    print(f'Do you want to create a new user account?')
    print ('1 - yes')
    print ('0 - no')
    create_user_prompt = int(input(''))

    if create_user_prompt == 0:
        return
    
    print(f'Enter the password for {employee_id}')
    password = input('')
    pw_key = generate_key(password)

    print(f'Enter desired access level:')
    print('1 - Cashier')
    print('2 - Manager')
    print('3 - Administrator')
    access_level = int(input(''))

    session.db_create_user(employee_id, pw_key, access_level)

#MAIN
    #LOGIN

# if login() == False:
#     print('Incorrect Employee ID or password')
#     exit()
# print('Login successfull')

    #DB SESSION
db_name = input('Enter DB name: ')
session = DatabaseSession(db_name)

print (f"Connect to DB '{db_name}'?")
print ('1 - yes')
print ('0 - no')

connect_prompt = int(input())

if connect_prompt == 1:
    session.connect_to_database()
elif connect_prompt == 0:
    exit()

menu = MainMenu()
while True:
    print(menu)
    menu.list_options()
    option = menu.choose_option()
    option.execute()
