import sqlite3
from people import create_employee, create_customer
from transactions import create_transaction
from datetime import date, datetime
from random import choice, randint

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
        print(f"Connected to DB '{db_name}'")

    def return_db_name(self):
        return self._db_name

#DATABASE MANAGEMENT

    def list_tables(self):
        table_list = self.cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table';").fetchall()
        for table in table_list:
            print(table)
            print()

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
        item_data = self.cursor.execute(f"SELECT * FROM Items WHERE name='{item_name}'").fetchall()
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

def database_selection_menu(db_name):
    print (f"Connect to DB '{db_name}'?")
    print ('1 - yes')
    print ('0 - no')
    connect_prompt = int(input())
    return connect_prompt



if __name__ == '__main__':
    db_name = input('Enter DB name: ')
    session = DatabaseSession(db_name)
    connect_prompt = database_selection_menu(db_name)
    if connect_prompt == 1:
        session.connect_to_database()
    while True:
        print(f'DB {db_name}.db')
        print()
        print('1 - transactions')
        print('2 - customers')
        print('3 - employees')
        print('4 - items')
        print('9 - manage database')
        action_prompt = int(input('Select action: '))
        if action_prompt == 1:
            while True:
                print('Transaction management')
                print()
                print('1 - list transactions')
                print('2 - create transactions')
                print('3 - delete transactions')
                print('0 - return')
                transaction_management_prompt = int(input(''))
                if transaction_management_prompt == 1:
                    session.db_list_transactions()
                elif transaction_management_prompt == 2:
                    while True:
                        print('Transaction creation')
                        print()
                        print('1 - create custom')
                        print('2 - create random')
                        print('3 - create multiple')
                        print('0 - return')
                        transaction_creation_prompt = int(input(''))
                        if transaction_creation_prompt == 1:
                            transaction_id = input('Transaction ID: ')
                            customer_id = int(input('Customer ID: '))
                            employee_id = input('Employee ID: ')
                            total = input('Total: ')
                            timestamp = datetime(input('Timestamp: '))
                            session.db_create_transaction(transaction_id, customer_id, employee_id, total, timestamp)
                            print(f'Transaction {transaction_id} created')
                            print()
                            while True:
                                item_to_add = input('Select item: ')
                                if item_to_add == '':
                                    break
                                item_data = session.db_fetch_item_data(item_to_add)
                                amount_to_add = int(input('Amount: '))
                                for item in range(amount_to_add):
                                    print(transaction_id, item_data[0], item_to_add, amount_to_add)
                                    session.db_itemize_transaction(transaction_id, item_data[0], item_to_add, amount_to_add)
                        elif transaction_creation_prompt == 2:
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
                        elif transaction_creation_prompt == 3:
                            transaction_number = int(input('Number of transactions: '))
                            if transaction_number == 0:
                                break
                            for number in range(transaction_number):
                                transaction_id, customer_id, employee_id, total, timestamp = create_transaction(session.db_list_customer_id(), session.db_list_employee_id(), 5.00)
                                print(transaction_id, customer_id, employee_id, total, timestamp)
                                session.db_create_transaction(transaction_id, customer_id, employee_id, total, timestamp)
                                print(f'Transaction {transaction_id} created')
                                list_of_items = session.db_return_items()
                                choosen_items = randint(1, len(list_of_items))
                                for item in range(choosen_items):
                                    item_data = choice(list_of_items)
                                    amount = randint(1, 10)
                                    session.db_itemize_transaction(transaction_id, item_data[0], item_data[1], amount)
                        elif transaction_creation_prompt == 0:
                            break
                elif transaction_management_prompt == 3:
                    print('Transaction deletion')
                    print()
                    print('1 - delete via ID')
                    print('2 - delete all')
                    print('0 - return')
                    transaction_deletion_prompt = int(input(''))
                    if transaction_deletion_prompt == 1:
                        transaction_id_prompt = input('Enter Transaction ID: ')
                        session.db_delete_transaction_id(transaction_id_prompt)
                    elif transaction_deletion_prompt == 2:
                        session.db_delete_transactions_all()
                    elif transaction_deletion_prompt == 0:
                        break  
                elif transaction_management_prompt == 0:
                    break                  
        elif action_prompt == 2:
            while True: 
                print('Customer management')
                print()
                print('1 - list customers')
                print('2 - create customers')
                print('3 - delete customers')
                print('0 - return')
                customer_management_prompt = int(input(''))
                if customer_management_prompt == 1:
                    session.db_list_customers()
                elif customer_management_prompt == 2:
                    while True:
                        print('Customer creation')
                        print()
                        print('1 - create custom')
                        print('2 - create random')
                        print('3 - create multiple')
                        print('0 - return')
                        customer_creation_prompt = int(input(''))
                        if customer_creation_prompt == 1:
                            f_name = input('First name: ')
                            l_name = input('Last name: ')
                            gender = input('Gender: ')
                            year = int(input('Year of birth: '))
                            month = int(input('Month: '))
                            day = int(input('Day: '))
                            dob = date(year, month, day)
                            customer_id = input('Customer ID:')
                            session.db_create_customer(f_name, l_name, gender, dob, customer_id)
                        elif customer_creation_prompt == 2:
                            f_name, l_name, gender, dob, customer_id = create_customer()
                            print (f_name, l_name, gender, dob, customer_id)
                            session.db_create_customer(f_name, l_name, gender, dob, customer_id)
                        elif customer_creation_prompt == 3:
                            customer_number = int(input('Number of customers: '))
                            if customer_number == 0:
                                break
                            for number in range(customer_number):
                                f_name, l_name, gender, dob, customer_id = create_customer()
                                print (f_name, l_name, gender, dob, customer_id)
                                session.db_create_customer(f_name, l_name, gender, dob, customer_id)
                        elif customer_creation_prompt == 0:
                            break      
                elif customer_management_prompt == 3:
                    print('Customer deletion')
                    print()
                    print('1 - delete via ID')
                    print('2 - delete all')
                    print('0 - return')
                    customer_deletion_prompt = int(input(''))
                    if customer_deletion_prompt == 1:
                        customer_id_prompt = int(input('Enter Customer ID: '))
                        session.db_delete_customer_id(customer_id_prompt)
                    elif customer_deletion_prompt == 2:
                        session.db_delete_customer_all()
                    elif customer_deletion_prompt == 0:
                        break
                elif customer_management_prompt == 0:
                    break
        elif action_prompt == 3:
            while True: 
                print('Employee management')
                print()
                print('1 - list employees')
                print('2 - create employees')
                print('3 - delete employees')
                print('0 - return')
                employee_management_prompt = int(input(''))
                if employee_management_prompt == 1:
                    session.db_list_employees()
                elif employee_management_prompt == 2:
                    while True:
                        print('Employee creation')
                        print()
                        print('1 - create custom')
                        print('2 - create random')
                        print('3 - create multiple')
                        print('0 - return')
                        employe_creation_prompt = int(input(''))
                        if employe_creation_prompt == 1:
                            f_name = input('First name: ')
                            l_name = input('Last name: ')
                            gender = input('Gender: ')
                            phone_no = int(input('Phone number: '))
                            employee_id = input('Employee ID:')
                            session.db_create_employee(f_name, l_name, gender, phone_no, employee_id)
                        elif employe_creation_prompt == 2:
                            f_name, l_name, gender, phone_no, employee_id = create_employee()
                            print (f_name, l_name, gender, phone_no, employee_id)
                            session.db_create_employee(f_name, l_name, gender, phone_no, employee_id)
                        elif employe_creation_prompt == 3:
                            employee_number = int(input('Number of employees: '))
                            if employee_number == 0:
                                break
                            for number in range(employee_number):
                                f_name, l_name, gender, phone_no, employee_id = create_employee()
                                print (f_name, l_name, gender, phone_no, employee_id)
                                session.db_create_employee(f_name, l_name, gender, phone_no, employee_id)
                        elif employe_creation_prompt == 0:
                            break      
                elif employee_management_prompt == 3:
                    while True:
                        print('Employee deletion')
                        print()
                        print('1 - delete via ID')
                        print('2 - delete all')
                        print('0 - return')
                        employee_deletion_prompt = int(input(''))
                        if employee_deletion_prompt == 1:
                            employee_id_prompt = input('Enter Employee ID: ')
                            session.db_delete_employee_id(employee_id_prompt)
                        elif employee_deletion_prompt == 2:
                            session.db_delete_employee_all()
                        elif employee_deletion_prompt == 0:
                            break
                elif employee_management_prompt == 0:
                    break
        elif action_prompt == 4:
            while True:
                print('Item management')
                print()
                print('1 - list items')
                print('2 - create item')
                print('3 - delete item')
                print('0 - return')
                item_management_prompt = int(input(''))
                if item_management_prompt == 1:
                    session.db_list_items()
                elif item_management_prompt == 2:
                    print('Item creation')
                    print()
                    print('1 - create custom')
                    print('2 - create standard list')
                    print('0 - return')
                    item_creation_prompt = int(input(''))
                    if item_creation_prompt == 1:
                        plu = int(input('Item PLU: '))
                        name = input('Item name:')
                        type = input('Type: ')
                        weight = float(input('Weight: '))
                        price = float(input('Price: '))
                        session.db_create_item(plu, name, type, weight, price)
                    elif item_creation_prompt == 2:
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
                    elif item_creation_prompt == 0:
                        break
                elif item_management_prompt == 3:
                    while True:
                        print('Item deletion')
                        print()
                        print('1 - delete via name')
                        print('2 - delete all')
                        print('0 - return')
                        item_deletion_prompt = int(input(''))
                        if item_deletion_prompt == 1:
                            item_name_prompt = input('Enter Item Name:')
                            session.db_delete_item_name(item_name_prompt)
                        elif item_deletion_prompt == 2:
                            session.db_delete_item_all()
                        elif item_deletion_prompt == 0:
                            break
                elif item_management_prompt == 0:
                    break
        elif action_prompt == 9:
            while True:
                print('DB management')
                print()
                print('1 - manage tables')
                print('2 - manage database')
                print('0 - return')
                manage_prompt = int(input(''))
                if manage_prompt == 1:
                    while True:
                        print('Table management')
                        print()
                        print('1 - list tables')
                        print('2 - create tables')
                        print('3 - drop table')
                        print('0 - return')
                        table_management_prompt = int(input(''))
                        if table_management_prompt == 1:
                            print(session.list_tables())
                        elif table_management_prompt == 2:
                            while True:
                                print('1 - transactions')
                                print('2 - customers')
                                print('3 - employees')
                                print('4 - items')
                                print('0 - return')
                                table_prompt = int(input(''))
                                if table_prompt == 1:
                                    session.db_create_transactions_table()
                                elif table_prompt == 2:
                                    session.db_create_customers_table()
                                elif table_prompt == 3:
                                    session.db_create_employees_table()
                                elif table_prompt == 4:
                                    session.db_create_items_table()
                                elif table_prompt == 0:
                                    break
                        elif table_management_prompt == 3:
                            table_name = input('Table name: ')
                            if table_name == '':
                                break
                            session.db_drop_table(table_name)
                        elif table_management_prompt == 0:
                            break
                elif manage_prompt == 2:
                    pass
                elif manage_prompt == 0:
                    break
