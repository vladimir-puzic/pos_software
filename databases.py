import sqlite3
from people import create_employee, create_customer
from datetime import date

class DatabaseSession:
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.connection = None

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
   
    def db_drop_table(self, table_name: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    def db_create_employee(self, f_name: str, l_name: str, gender: str, phone_no: int, employee_id: str):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Employees VALUES ('{f_name}', '{l_name}', '{gender}', '{phone_no}', '{employee_id}')")
        self.connection.commit()

    def db_list_employees(self):
        cursor = self.connection.cursor()
        employees_list = cursor.execute(f"SELECT * FROM Employees").fetchall()
        for employee in employees_list:
            print(employee)
    
    def db_delete_employee_id(self, employee_id: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Employees WHERE employee_id = '{employee_id}'")
        self.connection.commit()    
        pass

    def db_delete_employee_all(self):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Employees")
        self.connection.commit()       

    def db_create_customer(self, f_name: str, l_name: str, gender: str, dob: date, customer_id: int):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Customers VALUES ('{f_name}', '{l_name}', '{gender}', '{dob}', '{customer_id}')")
        self.connection.commit()

    def db_list_customers(self):
        cursor = self.connection.cursor()
        customers_list = cursor.execute(f"SELECT * FROM Customers").fetchall()
        for customer in customers_list:
            print(customer)
    
    def db_delete_customer_id(self, customer_id: str):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Customers WHERE customer_id = '{customer_id}'")
        self.connection.commit()    
        pass

    def db_delete_customer_all(self):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Customers")
        self.connection.commit()

if __name__ == '__main__':
    db_name = input('Enter DB name: ')
    session = DatabaseSession(db_name)
    print (f"Connect to DB '{db_name}'?")
    print ('1 - yes')
    print ('0 - no')
    connect_prompt = int(input())
    if connect_prompt == 1:
        session.connect_to_database()
    print(f"Connected to DB '{db_name}'")
    while True:
        print(f'DB {db_name}.db')
        print()
        print('1 - transactions')
        print('2 - customers')
        print('3 - employees')
        print('9 - manage database')
        action_prompt = int(input('Select action: '))
        if action_prompt == 9:
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
                                print('1 - employees')
                                print('2 - customers')
                                print('0 - return')
                                table_prompt = int(input(''))
                                if table_prompt == 1:
                                    session.db_create_employees_table()
                                elif table_prompt == 2:
                                    session.db_create_customers_table()
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
        elif action_prompt == 1:
            pass
        elif action_prompt == 2:
            while True: 
                print('Customer management')
                print()
                print('1 - list customers')
                print('2 - create customers')
                print('3 - drop customers')
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
                print('3 - drop employees')
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

    