# Student ID: 012054004

from datetime import timedelta
from Truck import Truck
from HashTable import HashTable
from data_loader import read_package_file, read_distance_file
from nearest_neighbor import deliver_packages

def main():
    filename = './WGUPS_CSV/Package_File.csv'
    #load info for trucks
    package_table = HashTable() # empty hashtable
    read_package_file(filename, package_table)
    distance_data, address_list = read_distance_file('./WGUPS_CSV/Distance_table.csv')
    print("Address List:", address_list)

    # trucks should now be able to be initialized
    truck1 = Truck(capacity=16, speed=18, address= 'HUB', depart_time=timedelta(hours=8))
    truck2 = Truck(capacity=16, speed=18, address= 'HUB', depart_time=timedelta(hours=9, minutes=5))
    truck3 = Truck(capacity=16, speed=18, address= 'HUB', depart_time=timedelta(hours=11))

    # Assign packages

    for i in range(1, 9): # 8 packages
        truck1.add_package(i, package_table)

    for i in range(9, 17): # 18 packages
        truck2.add_package(i, package_table)

    for i in range(17, 21):
        truck3.add_package(i, package_table)


    truck1.add_package(1, package_table)
    truck1.add_package(13, package_table)
    truck1.add_package(14, package_table)
    truck1.add_package(15, package_table)
    truck1.add_package(16, package_table)
    truck1.add_package(20, package_table)
    truck1.add_package(21, package_table)
    truck1.add_package(29, package_table)
    truck1.add_package(30, package_table)

    truck2.add_package(2, package_table)
    truck2.add_package(3, package_table)
    truck2.add_package(4, package_table)
    truck2.add_package(5, package_table)
    truck2.add_package(6, package_table)
    truck2.add_package(7, package_table)
    truck2.add_package(8, package_table)
    truck2.add_package(9, package_table)

    truck3.add_package(10, package_table)
    truck3.add_package(11, package_table)
    truck3.add_package(12, package_table)
    truck3.add_package(17, package_table)
    truck3.add_package(18, package_table)
    truck3.add_package(19, package_table)
    truck3.add_package(21, package_table)
    truck3.add_package(22, package_table)

    deliver_packages(truck1, package_table, distance_data, address_list)
    deliver_packages(truck2, package_table, distance_data, address_list)
    deliver_packages(truck3, package_table, distance_data, address_list)

    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage


if __name__ == "__main__":
    main()

