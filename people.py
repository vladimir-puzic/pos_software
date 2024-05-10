from datetime import datetime

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

if __name__ == '__main__':
    cust1 = Customer('Nikolina', 'Zubac', 'Female', datetime(1996, 4, 1), 558)
    print (cust1)
    emp1 = Employee('Vladimir', 'Puzic', 'Male', 65953513, 'vp553')
    print (emp1)
