#file contains code that manages user login and authentication

import database_management as dm
from random import choices, seed
from string import ascii_lowercase
import os

#LOGIN
def login():
    dm.connect_to_database('users')
    dm.db_create_users_table()


    for i in range(3):
        login_employee_id = 'vp123456' #input('Employee ID: ')
        password = ''#input('Password: ')

        if dm.db_check_user(login_employee_id) == False:
            if i < 2:
                print('User ID not found')
                continue
            print('User ID not found')
            print('Closing the application')
            exit()

        pw_key = generate_key(password)
        auth = dm.db_check_password(pw_key, login_employee_id)

        if auth == False:
            if i < 2:
                print('Incorrect password')
                continue
            print('Incorrect password')

            print('Do you want to reset your password?')
            print ('1 - yes')
            print ('0 - no')
            pw_reset_prompt = input('')
            if pw_reset_prompt == 0:
                exit()
            reset_password(login_employee_id)

        print('Login successfull')
        break

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

def reset_password(login_employee_id):
    print (dm.db_return_employee_data(login_employee_id))