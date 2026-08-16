from floor import Floor
from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, name, floor : list[Floor]):
        self.name = name
        self.floor = floor

    def find_parking(self, vehicle : Vehicle) -> ParkingSpot | None:
        for floor in self.floor:
            for parkingSpot in floor.parking_spots:
                if parkingSpot.available == True:
                    if parkingSpot.can_park(vehicle):
                        return parkingSpot
                    else:
                        continue
        return None

    