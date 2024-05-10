class Item:
    def __init__(self, name: str, type: str, weight: float, price: float):
        self._name = name
        self._type = type
        self._price = price
        self._weight = weight
    
    def __str__(self):
        return f'{self._name} ({self._type}) - Weight: {self._weight} kg / Price: {self._price:.2f} KM'
    
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