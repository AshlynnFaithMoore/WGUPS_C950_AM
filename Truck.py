# calculate routes, track mileage, and update delivery times/statuses.
from datetime import timedelta

class Truck:
    def __init__(self, capacity, speed, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.packages = []
        self.mileage = 0.0 # starting mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time


    def add_package(self, package_id, package_table):
    # Look up the actual package object
        package = package_table.lookup(package_id)

        if package is None:
            print(f"Warning: No package found for ID {package_id}")
            return None

        if len(self.packages) >= self.capacity:
            print("Package capacity exceeded")
            return None

    # Prevent duplicates
        if package_id in self.packages:
            print(f"Package {package_id} is already on the truck.")
            return None

        self.packages.append(package_id)
        return package

    def update_mileage(self, mileage):
        travel_time = timedelta(hours= mileage / self.speed)
        self.time += travel_time
        self.mileage += mileage

    # to read and debug
    def __str__(self):
        return (f"Truck(address={self.address}, mileage={self.mileage:.2f}, "
                f"time={self.time}, packages={self.packages})")






