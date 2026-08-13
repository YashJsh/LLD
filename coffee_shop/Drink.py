from CoffeeEnums import CoffeeType, Size, Topping

class Drink:
    def __init__(
        self, 
        coffee_type : CoffeeType,
        size : Size, 
        toppings : list[Topping], 
        extra_shots
    ):
        self.coffee_type = coffee_type
        self.size = size
        self.toppings = toppings
        self.extra_shots = extra_shots 




