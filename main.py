# Student ID: 012054004

from datetime import timedelta
from Truck import Truck
from HashTable import HashTable
from data_loader import read_package_file, read_distance_file
from nearest_neighbor import deliver_packages

def main():
    filename = './WGUPS_CSV/Package_File.csv'
    #load info for trucks
    package_hash = HashTable() # empty hashtable
    read_package_file(filename, package_hash)
    distance_data, address_list = read_distance_file('./WGUPS_CSV/Distance_table.csv')

    # trucks should now be able to be initialized

    truck1 = Truck(capacity=16, speed=18, address="HUB", depart_time=timedelta(hours=8))
    truck2 = Truck(capacity=16, speed=18, address="HUB", depart_time=timedelta(hours=9, minutes=5))
    truck3 = Truck(capacity=16, speed=18, address="HUB", depart_time=timedelta(hours=11))

    # Assign packages

    for i in range(1, 9): # 8 packages
        truck1.add_package(i)

    for i in range(9, 17): # 18 packages
        truck2.add_package(i)

    for i in range(17, 21):
        truck3.add_package(i)

    # Deliver packages deliver_packages(truck1, package_hash, distance_data, address_list) deliver_packages(truck2, package_hash, distance_data, address_list) # Show mileage total_mileage = truck1.mileage + truck2.mileage print(f"Total mileage: {total_mileage:.2f} miles")

if __name__ == "__main__":
    main()

