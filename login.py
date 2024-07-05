import database_management
from random import choice, choices, randint, seed
from string import ascii_lowercase
from os import path

#LOGIN
def login():
    database_management.connect_to_database('users')
    database_management.db_create_users_table()

    login_employee_id = input('Employee ID: ')
    password = input('Password: ')

    if database_management.db_check_user(login_employee_id) == False:
        exit()
    
    pw_key = generate_key(password)
    auth = database_management.db_check_password(pw_key, login_employee_id)

    return auth, login_employee_id

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