from datetime import datetime, date, timedelta
from random import randint, choice

class Person:
    def __init__(self, f_name: str, l_name: str, gender: str):
        self._f_name = f_name
        self._l_name = l_name
        self._gender = gender

class Customer(Person):
    def __init__(self, f_name: str, l_name: str, gender: str, dob: datetime, id: int):
        super().__init__(f_name, l_name, gender)
        self._dob = dob
        self._id = id
    
    def __str__(self):
        return f'{self._id}: {self._f_name} {self._l_name} ({self._gender}) Date of birth: {self._dob.strftime("%d.%m.%Y")}'

class Employee(Person):
    def __init__(self, f_name: str, l_name: str, gender: str, phone_no: int, employee_id: str):
        super().__init__(f_name, l_name, gender)
        self._phone_no = phone_no
        self._employee_id = employee_id
    
    def __str__(self):
        return f'{self._employee_id}: {self._f_name} {self._l_name} ({self._gender}) Phone number: {self._phone_no}'

def random_date(start, end):
    delta = end - start
    

def create_employee():
    genders = ['Female', 'Male']
    gender = choice(genders)

    if gender == 'Female':
        names = []
        with open('female_names.txt', 'r') as file:
           for name in file:
               names.append(name.strip())
        f_name = choice(names)
    elif gender == 'Male':
        names = []
        with open('male_names.txt', 'r') as file:
           for name in file:
               names.append(name.strip())
        f_name = choice(names)

    l_names = []
    with open('last_names.txt', 'r') as file:
        for name in file:
            names.append(name.strip())
    l_name = choice(names)

    phone_no = int(f'6{randint(1,6)}{randint(000000,999999):06d}')

    employee_id = (f'{f_name[0].lower()}{l_name[0].lower()}{randint(000000,999999)}')
    return [f_name, l_name, gender, phone_no, employee_id]

def create_customer():
    genders = ['Female', 'Male']
    gender = choice(genders)

    if gender == 'Female':
        names = []
        with open('female_names.txt', 'r') as file:
           for name in file:
               names.append(name.strip())
        f_name = choice(names)
    elif gender == 'Male':
        names = []
        with open('male_names.txt', 'r') as file:
           for name in file:
               names.append(name.strip())
        f_name = choice(names)

    l_names = []
    with open('last_names.txt', 'r') as file:
        for name in file:
            names.append(name.strip())
    l_name = choice(names)

    range_lenght = date.today() - date(1900, 1, 1)
    total_days = range_lenght.days
    dob = date(1900, 1, 1) + timedelta(days=choice(range(total_days)))

    id = int(f'{randint(000000,999999):06d}')
    
    return [f_name, l_name, gender, dob, id]


if __name__ == '__main__':
    cust1 = Customer('Nikolina', 'Zubac', 'Female', datetime(1996, 4, 1), 558)
    print (cust1)
    emp1 = Employee('Vladimir', 'Puzic', 'Male', 65953513, 'vp553')
    print (emp1)
    f_name, l_name, gender, phone_no, employee_id = create_employee()
    emp2 = Employee(f_name, l_name, gender, phone_no, employee_id)
    print (emp2)
    f_name, l_name, gender, dob, id = create_customer()
    cust2 = Customer(f_name, l_name, gender, dob, id)
    print (cust2)
