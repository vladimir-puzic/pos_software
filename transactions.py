from people import Person, Customer, Employee
from datetime import datetime
from random import randint, choice

class Item:
    def __init__(self, name: str, type: str, weight: float, price: float):
        self._name = name
        self._type = type
        self._price = price
        self._weight = weight
    
    def __str__(self):
        return f'{self._name} ({self._type}) - Weight: {self._weight} kg / Price: {self._price:.2f} KM'

class Transaction:
    def __init__(self, transaction_id: str, customer_id: int, employee_id: str, timestamp: datetime):
        self._transactions_id = transaction_id
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

if __name__ == '__main__':
    milk = Item('Milk', 'Dairy', 1, 2.50)
    print (milk)
    eggs = Item('Eggs', 'Dairy' , 0.5, 3.00)
    print (eggs)
    cheese = Item('Cheese', 'Dairy', 1, 10.00)
    print (cheese)
    bread = Item('Bread', 'Baked Goods', 0.5, 1.60)
    print (bread)
    coffee = Item('Coffee', 'Beverages', 0.5, 5.00)
    print (coffee)
    juice = Item('Juice', 'Beverages', 1, 3.50)
    print (juice)
    pork = Item('Pork', 'Meat', 1, 13)
    print (pork)
    chicken_breast = Item('Chicken Breast', 'Meat', 1, 10)
    print (chicken_breast)
    pass