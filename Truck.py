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

    def add_package(self, packageID):
        if len(self.packages) < self.capacity:
            self.packages.append(packageID)
        else:
            print("Package capacity exceeded")

    def update_mileage(self, mileage):
        travel_time = timedelta(hours= mileage / self.speed)
        self.time += travel_time
        self.mileage += mileage

    # to read and debug
    def __str__(self):
        return (f"Truck(address={self.address}, mileage={self.mileage:.2f}, "
                f"time={self.time}, packages={self.packages})")






