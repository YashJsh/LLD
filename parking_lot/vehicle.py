class Vehicle:
    def __init__(self, vehicle_type, number: str):
        self.vehicle_type = vehicle_type 
        self.vehicle_number = number

class Bike(Vehicle):
    def __init__(self, number):
        super().__init__("Bike", number)

class Car(Vehicle):
    def __init__(self, number):
        super().__init__("Car", number)

class Truck(Vehicle):
    def __init__(self, number):
        super().__init__("Truck", number)
