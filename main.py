from datetime import date, datetime

import session as s
import database_management as dm
from menu_screens import MainMenu
from login import login

#MAIN
    #DB SESSION
login()
s.s_db_name = input('Enter DB name: ')

print (f"Connect to DB '{s.s_db_name}'?")
print ('1 - yes')
print ('0 - no')

connect_prompt = int(input())

if connect_prompt == 1:
    dm.connect_to_database(s.s_db_name)
elif connect_prompt == 0:
    exit()

s.s_menu = MainMenu(s.s_db_name)
while True:
    print(s.s_menu)
    s.s_menu.list_options()
    s.s_option = s.s_menu.choose_option()
    s.s_option.execute(s.s_db_name)
