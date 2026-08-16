from vehicle import Vehicle
from parking_types import ParkingSpotTypes

class ParkingSpot:
    vehicle_number : str | None
    def __init__(self, spot_id, spot_size : ParkingSpotTypes, available = True):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.available = available

    def can_park(self, vehicle: Vehicle):
        if (vehicle.vehicle_type == "Car" and self.spot_size == ParkingSpotTypes.LARGE or vehicle.vehicle_type == "Car" and self.spot_size == ParkingSpotTypes.SMALL):
            return False
        elif (vehicle.vehicle_type == "Bike" and self.spot_size == ParkingSpotTypes.LARGE or vehicle.vehicle_type == "Bike" and self.spot_size == ParkingSpotTypes.MEDIUM):
            return False
        elif (vehicle.vehicle_type == "Truck" and self.spot_size == ParkingSpotTypes.SMALL or vehicle.vehicle_type == "Truck" and self.spot_size == ParkingSpotTypes.MEDIUM):
            return False
        if (self.available == True):
            return True

    def park(self, vehicle: Vehicle):
        self.available = False
        self.vehicle_number = vehicle.vehicle_number

    def remove_vehicle(self):
        self.available = True
        self.vehicle_number = None
