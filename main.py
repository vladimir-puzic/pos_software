from datetime import date, datetime
from random import choice, choices, randint, seed
from string import ascii_lowercase

import session as s
import database_management
from menu_screens import MainMenu

#MAIN
    #LOGIN
# auth, user_id = login()

# if auth == False:
#     print('Incorrect Employee ID or password')
#     exit()
# print('Login successfull')


    #DB SESSION
s.s_db_name = input('Enter DB name: ')

print (f"Connect to DB '{s.s_db_name}'?")
print ('1 - yes')
print ('0 - no')


connect_prompt = int(input())

if connect_prompt == 1:
    database_management.connect_to_database(s.s_db_name)
elif connect_prompt == 0:
    exit()

s.s_menu = MainMenu(s.s_db_name)
while True:
    print(s.s_menu)
    s.s_menu.list_options()
    s.s_option = s.s_menu.choose_option()
    s.s_option.execute(s.s_db_name)
