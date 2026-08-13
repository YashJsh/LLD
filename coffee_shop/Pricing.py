from Drink import Drink
from CoffeeEnums import CoffeeType, Topping, Size

class Pricing:
    def __init__(self):
        self.coffee_prices = {
            CoffeeType.AMERICANO : 120,
            CoffeeType.CAPPUCCINO : 100,
            CoffeeType.ESPRESSO: 100,
            CoffeeType.LATTE: 150,
            CoffeeType.MOCHA: 180
        }

        self.size_prices = {
            Size.LARGE : 40,
            Size.MEDIUM : 20,
            Size.SMALL : 0
        }

        self.topping_prices = {
            Topping.CARAMEL_SYRUP :30,
            Topping.CHOCOLATE_DRIZZLE : 20,
            Topping.CINNAMON : 50,
            Topping.VANILLA_SYRUP : 15,
            Topping.WHIPPED_CREAM :  10
        }

        self.extra_shot_price = 30


    def calculate_price(self, drink: Drink):
        total = 0

        total += self.coffee_prices[drink.coffee_type]
        total += self.size_prices[drink.size]

        for topping in drink.toppings:
            total += self.topping_prices[topping]

        total += self.extra_shot_price * drink.extra_shots

        return total
        