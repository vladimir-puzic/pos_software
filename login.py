#file contains code that manages user login and authentication

import database_management as dm
import session as s
from random import choices, seed
from string import ascii_lowercase, digits
import os
from datetime import datetime, timedelta 

#LOGIN
def login():
    dm.connect_to_database('users')
    dm.db_create_users_table()


    for i in range(3):
        login_employee_id = input('Employee ID: ')
        password = input('Password: ')

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
            account_recovery(login_employee_id)

        print('Login successfull')
        break

    return auth, login_employee_id

def generate_key(password):
    seed(password)
    pw_key = ''.join(choices(ascii_lowercase, k=16))

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

def token_generate():
    seed()
    pw_reset_token = ''.join(choices(digits, k=6))
    return pw_reset_token

def token_check(token: int, token_gen_time: datetime):
    token_input = input('Password reset token: ')
    if token_input != token:
        print('Incorrect password reset token')
        print('Closing the application')
        exit()
    
#    print (datetime.now() - token_gen_time)
#    print (timedelta(seconds=5))
    elif datetime.now() - token_gen_time > timedelta(minutes=5):
        print('Token expired')
        print('Closing the application')
        exit()
    pass

def reset_password(login_employee_id):
    while True:
        new_pass = input('Enter new passowrd: ')
        new_pass_check = input('Enter password again: ')
        if new_pass == new_pass_check:
            break
    new_pw_key = generate_key(new_pass)
    dm.db_change_password(login_employee_id, new_pw_key)


def account_recovery(login_employee_id):
    user_email = (dm.db_return_user_data(login_employee_id)[3])
    token = token_generate()
    with open(f'{user_email}', 'w') as file:
        file.write(f'{token}')
    print('Password reset token has been generated and delivered to your email address')
    print('The token expires after 5 minutes')

    token_check(token, datetime.now())
    reset_password(login_employee_id)
    
    print ('Your password has been reset')


