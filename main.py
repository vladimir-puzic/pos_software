from datetime import date, datetime
from random import choice, choices, randint, seed
from string import ascii_lowercase

import database_session
from menu_screens import MainMenu

#LOGIN
# def login():
#     database_session.connect_to_database('users')
#     database_session.db_create_users_table()

#     login_employee_id = input('Employee ID: ')
#     password = input('Password: ')



#     if database_session.db_check_user(login_employee_id) == False:
#         exit()
    
#     pw_key = generate_key(password)
#     auth = database_session.db_check_password(pw_key, login_employee_id)

#     return auth, login_employee_id

# def generate_key(password):
#     seed(password)
#     char_list = choices(ascii_lowercase, k=16)
#     pw_key = ''.join(char_list)

#     return pw_key

# def create_user(employee_id, session):
#     print(f'Employee {employee_id} does not exist.')
#     print(f'Do you want to create a new user account?')
#     print ('1 - yes')
#     print ('0 - no')
#     create_user_prompt = int(input(''))

#     if create_user_prompt == 0:
#         return
    
#     print(f'Enter the password for {employee_id}')
#     password = input('')
#     pw_key = generate_key(password)

#     print(f'Enter desired access level:')
#     print('1 - Cashier')
#     print('2 - Manager')
#     print('3 - Administrator')
#     access_level = int(input(''))

#     session.db_create_user(employee_id, pw_key, access_level)

#MAIN
    #LOGIN
# auth, user_id = login()

# if auth == False:
#     print('Incorrect Employee ID or password')
#     exit()
# print('Login successfull')


    #DB SESSION
db_name = input('Enter DB name: ')

print (f"Connect to DB '{db_name}'?")
print ('1 - yes')
print ('0 - no')


connect_prompt = int(input())

if connect_prompt == 1:
    database_session.connect_to_database(db_name)
elif connect_prompt == 0:
    exit()

menu = MainMenu(db_name)
while True:
    print(menu)
    menu.list_options()
    option = menu.choose_option()
    option.execute(option, menu)
