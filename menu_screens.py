from people import create_employee, create_customer
from transactions import create_transaction
from datetime import date, datetime
from random import choice, choices, randint, seed

from database_session import *
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

    def execute(self, option, menu):
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
    def __init__(self, db_name) -> None:
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
        self._function = db_list_transactions

    def execute(self):
        self._function()

#Create Transactions
    #Create Transaction Custom

class CreateTransactionCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Transaction'
        self._function = db_create_transaction
    
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
            item_data = db_fetch_item_data(item_to_add)
            amount_to_add = int(input('Amount: '))
            for item in range(amount_to_add):
                print(transaction_id, item_data[0], item_data[1], amount_to_add)
                db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount_to_add)

    #Create Transaction Random

class CreateTransactionRandom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Random Transaction'
        self._function = db_create_transaction

    def execute(self):
        transaction_id, customer_id, employee_id, total, timestamp = create_transaction(db_list_customer_id(), db_list_employee_id(), 5.00)
        print(transaction_id, customer_id, employee_id, total, timestamp)
        self._function(transaction_id, customer_id, employee_id, total, timestamp)
        print(f'Transaction {transaction_id} created')
        list_of_items = db_return_items()
        choosen_items = randint(1, (len(list_of_items)))
        for item in range(choosen_items):
            item_data = choice(list_of_items)
            amount = randint(1, 10)
            db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount)

    #Create Transaction Multiple
    
class CreateTransactionMultiple(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Multiple Transactions'
        self._function = db_create_transaction

    def execute(self):
        transaction_number = int(input('Number of transactions: '))
        if transaction_number == 0:
            return
        for number in range(transaction_number):
            transaction_id, customer_id, employee_id, total, timestamp = create_transaction(db_list_customer_id(), db_list_employee_id(), 5.00)
            print(transaction_id, customer_id, employee_id, total, timestamp)
            self._function(transaction_id, customer_id, employee_id, total, timestamp)
            print(f'Transaction {transaction_id} created')
            list_of_items = db_return_items()
            choosen_items = randint(1, len(list_of_items))
            for item in range(choosen_items):
                item_data = choice(list_of_items)
                amount = randint(1, 10)
                db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount)

#Delete Transactions
    #Delete Transaction via ID

class DeleteTransactionID(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Transaction via ID'
        self._function = db_delete_transaction_id

    def execute(self):
        transaction_id_prompt = input('Enter Transaction ID: ')
        self._function(transaction_id_prompt)

    #Delete Transaction All

class DeleteTransactionAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Transactions'
        self._function = db_delete_transactions_all
    
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
        self._function = db_list_customers
    
    def execute(self):
        self._function()

#Create Customers
    #Create Customer Custom

class CreateCustomerCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Customer'
        self._function = db_create_customer
    
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
        self._function = db_create_customer
    
    def execute(self):
        f_name, l_name, gender, dob, customer_id = create_customer()
        print (f_name, l_name, gender, dob, customer_id)
        self._function(f_name, l_name, gender, dob, customer_id)

    #Create Customer Multiple

class CreateCustomerMultiple(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Multiple Customers'
        self._function = db_create_customer
    
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
        self._function = db_delete_customer_id

    def execute(self):
        customer_id_prompt = int(input('Enter Customer ID: '))
        self._function(customer_id_prompt)

    #Delete Customer All

class DeleteCustomerAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Customers'
        self._function = db_delete_customer_all
    
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
        self._function = db_list_employees
    
    def execute(self):
        self._function()

#Create Employees
    #Create Employees Custom

class CreateEmployeeCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Employee'
        self._function = db_create_employee
    
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
        self._function = db_create_employee
    
    def execute(self):
        f_name, l_name, gender, phone_no, employee_id = create_employee()
        print (f_name, l_name, gender, phone_no, employee_id)
        self._function(f_name, l_name, gender, phone_no, employee_id)  

    #Create Employee Multiple

class CreateEmployeeMultiple(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Multiple Employees'
        self._function = db_create_employee
    
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
        self._function = db_delete_employee_id
    
    def execute(self):
        employee_id_prompt = input('Enter Employee ID: ')
        self._function(employee_id_prompt)        

    #Delete Employee All

class DeleteEmployeeAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Employees'
        self._function = db_delete_employee_all
    
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
        self._function = db_list_items
    
    def execute(self):
        self._function()

#Create Items
    #Create Custom Item

class CreateItemCustom(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Create Custom Item'
        self._function = db_create_item
    
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
        self._function = db_create_item
    
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
            db_create_item(plu, name, type, weight, price)

#Delete Items
    #Delete Items via Name

class DeleteItemName(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete Item via Name'
        self._function = db_delete_item_name
    
    def execute(self):
        item_name_prompt = input('Enter Item Name:')
        self._function(item_name_prompt)
        
    #Delete Items All

class DeleteItemAll(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Delete All Items'
        self._function = db_delete_item_all
    
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
        self._function = db_list_tables

#Create Tables
    #Create Transactions Table

class CreateTableTransactions(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Transactions Table'
        self._function = db_create_transactions_table

    #Create Customers Table

class CreateTableCustomers(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Customers Table'
        self._function = db_create_customers_table

    #Create Employees Table

class CreateTableEmployees(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Employees Table'
        self._function = db_create_employees_table

    #Create Items Table

class CreateTableItems(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._header = 'Items Table'
        self._function = db_create_items_table
