# 1
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author
    
    def read(self):
        print(f"Book Information: {self.name} by {self.author}")
        print(f"Price: ${self.price}, Quantity: {self.quantity}")
"""
# 2
"""
class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, Drive_thru):
        super().__init__(name, cuisine, menu)
        self.Drive_thru = Drive_thru

    def order(self, dish_name, quantity):
        if dish_name in self.menu:
            if quantity <= self.menu[dish_name]['quantity']:
                self.menu[dish_name]['quantity'] -= quantity
                return self.menu[dish_name]['price'] * quantity
            else:
                return "Requested quantity not available"
        else:
            return "Dish not available"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))
print(mc.order('burger', 15))
print(mc.order('soup', 5))
"""