from Drink import Drink
from Pricing import Pricing

class Order:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.drinks: list[Drink] = []

    def print_order_owner(self):
        return f"Order placed by {self.name} of age {self.age}"

    def add_drink(self, drink: Drink):
        self.drinks.append(drink)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def remove_all_drinks(self):
        self.drinks.clear()

    def get_total_price(self, pricing: Pricing):
        total = 0
        for drink in self.drinks:
            total += pricing.calculate_price(drink)

        return total
