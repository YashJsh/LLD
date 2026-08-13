from enum import Enum

class CoffeeType(Enum):
    ESPRESSO = "Espresso"
    AMERICANO = "Americano"
    LATTE = "Latte"
    CAPPUCCINO = "Cappuccino"
    MOCHA = "Mocha"

class Size(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class Topping(Enum):
    WHIPPED_CREAM = "Whipped_Cream"
    CARAMEL_SYRUP = "Caramel_Syrup"
    VANILLA_SYRUP = "Vanilla_Syrup"
    CHOCOLATE_DRIZZLE = "Cholocate_Drizzle"
    CINNAMON = "Cinnamon"



