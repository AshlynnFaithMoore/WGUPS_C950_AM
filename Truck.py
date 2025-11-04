# calculate routes, track mileage, and update delivery times/statuses.
from datetime import timedelta

class Truck:
    # The truck class maintains the trucks current location, time, mileage, and list of packages.
    #     As the truck travels to deliver packages, its time and mileage are automatically
    #     updated based on distance traveled and truck speed.
    #
    #     Key Constraints given in instructions:
    #         Maximum capacity: 16 packages
    #         Speed: 18 miles per hour (constant)
    #         Must return to hub after completing deliveries
    def __init__(self, capacity, speed, address, depart_time):
        #Initializing a new Truck object with specified parameters.
        self.capacity = capacity
        self.speed = speed
        self.packages = [] #List of package IDs currently on truck (empty initially)
        self.mileage = 0.0 # starting mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time #Current time (starts at depart_time, updates as truck travels)


    def add_package(self, package_id, package_table):
        #Adds a package to the truck's cargo by package ID.

        #This method performs validation checks before adding the package:
        #Verifies package exists in the hash table
        #Checks truck capacity hasn't been exceeded
        #Prevents duplicate packages from being added
        package = package_table.lookup(package_id)
        # checks if package exists
        if package is None:
            print(f"Warning: No package found for ID {package_id}")
            return None
        # checks if capacity is exceeded or equal to the amount of packages in truck
        if len(self.packages) >= self.capacity:
            print("Package capacity exceeded")
            return None

    # Prevent duplicates
        if package_id in self.packages:
            print(f"Package {package_id} is already on the truck.")
            return None
        # add package ID only after all validations passed
        self.packages.append(package_id)
        return package

    def update_mileage(self, mileage):
        # Update truck's mileage and current time based on distance traveled.

        # This method is called each time the truck moves to a new location.

        # Calculate travel time using speed

        travel_time = timedelta(hours= mileage / self.speed)
        # update current time and mileage
        self.time += travel_time
        self.mileage += mileage

    # to read and debug
    def __str__(self):
        return (f"Truck(address={self.address}, mileage={self.mileage:.2f}, "
                f"time={self.time}, packages={self.packages})")






