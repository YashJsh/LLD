from parking_lot import ParkingLot
from floor import Floor
from parking_spot import ParkingSpot
from parking_types import ParkingSpotTypes
from vehicle import Car, Bike, Truck


def park_vehicle(lot: ParkingLot, vehicle):
    spot = lot.find_parking(vehicle)
    if not isinstance(spot, ParkingSpot):
        print(f"{vehicle.vehicle_type} ({vehicle.vehicle_number}): NO Parking Spot left")
        return
    print(f"{vehicle.vehicle_type} ({vehicle.vehicle_number}) found spot: {spot.spot_id}")
    spot.park(vehicle)
    print(f"After parking -> available: {spot.available}, vehicle: {spot.vehicle_number}")


def main():
    spot1 = ParkingSpot(1, ParkingSpotTypes.SMALL)
    spot2 = ParkingSpot(2, ParkingSpotTypes.MEDIUM)
    spot3 = ParkingSpot(3, ParkingSpotTypes.LARGE)
    spot4 = ParkingSpot(4, ParkingSpotTypes.SMALL)
    spot5 = ParkingSpot(5, ParkingSpotTypes.MEDIUM)

    floor1 = Floor(1, [spot1, spot2, spot3])
    floor2 = Floor(2, [spot4, spot5])

    lot = ParkingLot("MyParkingLot", [floor1, floor2])

    car = Car("KA-01-1234")
    park_vehicle(lot, car)

    bike = Bike("KA-02-9999")
    park_vehicle(lot, bike)

    truck = Truck("KA-03-5555")
    park_vehicle(lot, truck)

    print(f"\nParking {car.vehicle_number} again (should find an available spot)")
    park_vehicle(lot, car)

    print(f"\nRemoving {truck.vehicle_number} from spot {spot3.spot_id}")
    spot3.remove_vehicle()
    print(f"After removal -> available: {spot3.available}, vehicle: {spot3.vehicle_number}")

    print("\nChecking if any spots are left for more vehicles")
    park_vehicle(lot, Car("KA-04-0001"))
    park_vehicle(lot, Bike("KA-05-0002"))


if __name__ == "__main__":
    main()
