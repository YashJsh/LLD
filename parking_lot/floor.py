from parking_spot import ParkingSpot

class Floor:
    def __init__(self, floor_number, parking_spots : list[ParkingSpot]):
        self.floor_number = floor_number
        self.parking_spots = parking_spots