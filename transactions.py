#file contains code for creating Items and Transactions

from people import Person, Customer, Employee
from datetime import datetime
from random import randint, choice

class Item:
    def __init__(self, plu: int, name: str, type: str, weight: float, price: float):
        self._plu = plu
        self._name = name
        self._type = type
        self._price = price
        self._weight = weight
    
    def __str__(self):
        return f'{self._name} ({self._type}) - Weight: {self._weight} kg / Price: {self._price:.2f} KM'

class Transaction:
    def __init__(self, transaction_id: str, customer_id: int, employee_id: str, timestamp: datetime):
        self._transaction_id = transaction_id
        self._customer_id = customer_id
        self._employee_id = employee_id
        self._total = None
        self._timestamp = timestamp

def create_transaction(customer_id_list: list, employee_id_list: list, sum_total: float):
    timestamp = datetime.now()

    transaction_id = f'{timestamp.year}{timestamp.month:02d}{timestamp.day:02d}-{randint(000000, 999999):06d}' 

    customer_id = (choice(customer_id_list))[0]

    employee_id = (choice(employee_id_list))[0]

    total = sum_total

    return [transaction_id, customer_id, employee_id, total, timestamp]

def itemize(transaction_id: str):
    pass

if __name__ == '__main__':
    #placeholder items, used for testing
    milk = Item(644455, 'Milk', 'Dairy', 1, 2.50)
    print (milk)
    eggs = Item(994111, 'Eggs', 'Dairy' , 0.5, 3.00)
    print (eggs)
    cheese = Item(222449, 'Cheese', 'Dairy', 1, 10.00)
    print (cheese)
    bread = Item(227779, 'Bread', 'Baked Goods', 0.5, 1.60)
    print (bread)
    coffee = Item(222666, 'Coffee', 'Beverages', 0.5, 5.00)
    print (coffee)
    juice = Item(588444, 'Juice', 'Beverages', 1, 3.50)
    print (juice)
    pork = Item(766611, 'Pork', 'Meat', 1, 13)
    print (pork)
    chicken_breast = Item(222444, 'Chicken Breast', 'Meat', 1, 10)
    print (chicken_breast)
    pass