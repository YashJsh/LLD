from CoffeeEnums import CoffeeType, Size, Topping
from Drink import Drink
from Order import Order
from Pricing import Pricing

def main():
    pricing = Pricing()

    latte = Drink(
        coffee_type=CoffeeType.LATTE,
        size=Size.LARGE,
        toppings=[
            Topping.CARAMEL_SYRUP,
            Topping.VANILLA_SYRUP
        ],
        extra_shots=1
    )

    mocha = Drink(
        coffee_type=CoffeeType.MOCHA,
        size=Size.MEDIUM,
        toppings=[
            Topping.WHIPPED_CREAM
        ],
        extra_shots=0
    )

    order = Order("Yash", 18)

    order.add_drink(latte)
    order.add_drink(mocha)

    print(order.print_order_owner())
    print("Latte Price:", pricing.calculate_price(latte))
    print("Mocha Price:", pricing.calculate_price(mocha))
    print("Order Total:", order.get_total_price(pricing))


if __name__ == "__main__":
    main()