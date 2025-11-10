# Student ID: 012054004

from datetime import timedelta, datetime
from Truck import Truck
from HashTable import HashTable
from data_loader import read_package_file, read_distance_file
from nearest_neighbor import deliver_packages

def main():
    """

        Main function to initialize and run the WGUPS package delivery system.
        Loads package data, creates trucks, assigns packages, delivers them using
        nearest neighbor algorithm, and provides user interface for status queries.
        """
    package_filename = './WGUPS_CSV/Package_File.csv'
    distance_filename = './WGUPS_CSV/Distance_table.csv'
    #loading the package information into the Hashtable for trucks
    package_table = HashTable() # empty hashtable
    read_package_file(package_filename, package_table)
    # loading distance information for routing
    distance_data, address_list = read_distance_file(distance_filename)
    print("Address List:", address_list)

    # trucks should now be able to be initialized
    # truck1 departs at 8AM
    truck1 = Truck(capacity=16, speed=18, address= 'HUB', depart_time=timedelta(hours=8))
    #truck2 departs at 9:05 to account for the late packages
    truck2 = Truck(capacity=16, speed=18, address= 'HUB', depart_time=timedelta(hours=9, minutes=5))
    # truck3 departs at 10:20 when one truck returns (only 2 drivers)
    truck3 = Truck(capacity=16, speed=18, address= 'HUB', depart_time=timedelta(hours=10, minutes=20))

    # Handle special constraint: Package 9 has wrong address until 10:20 AM
    # CSV contains "300 State St" but correct address is "410 S State St"
    # Since truck 3 departs at 10:20, we update the address now (simulating the correction)
    package_9 = package_table.lookup(9)
    if package_9:
        package_9.address = "410 S State St"
        package_9.city = "Salt Lake City"
        package_9.state = "UT"
        package_9.zipcode = "84111"

    # Assign packages - manually
    # - Packages with early deadlines go on truck 1
    # - Packages delayed until 9:05 and with "truck 2 only" constraint go on truck 2
    # - Remaining packages get distributed to truck 3

    truck1_packages = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
    for pkg_id in truck1_packages:
        truck1.add_package(pkg_id, package_table)
        package = package_table.lookup(pkg_id)
        if package:
            package.departure_time = truck1.depart_time

    truck2_packages = [3, 6, 18, 25, 28, 32, 36, 38, 2, 4, 5, 7, 8, 10]
    for pkg_id in truck2_packages:
        truck2.add_package(pkg_id, package_table)
        package = package_table.lookup(pkg_id)
        if package:
            package.departure_time = truck2.depart_time

    truck3_packages = [9, 11, 12, 17, 19, 21, 22, 23, 24, 26, 27, 33, 35, 39]
    for pkg_id in truck3_packages:
        truck3.add_package(pkg_id, package_table)
        package = package_table.lookup(pkg_id)
        if package:
            package.departure_time = truck3.depart_time


    # Deliver packages using nearest neighbor algorithm
    deliver_packages(truck1, package_table, distance_data, address_list)
    deliver_packages(truck2, package_table, distance_data, address_list)
    deliver_packages(truck3, package_table, distance_data, address_list)

    # Calculate total mileage across all trucks for customer display
    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    print("Delivery Complete")
    print(f"Truck 1 Mileage: {truck1.mileage:.2f} miles")
    print(f"Truck 2 Mileage: {truck2.mileage:.2f} miles")
    print(f"Truck 3 Mileage: {truck3.mileage:.2f} miles")
    print(f"Total Mileage: {total_mileage:.2f} miles\n")

    user_interface(package_table, total_mileage)


def user_interface(package_table, total_mileage):
    """
        Provides an interactive command-line interface for users per instructions to:
        1. View status of a single package at a specific time
        2. View status of all packages at a specific time
        3. View total mileage
        4. Exit the program
    """
    print("Welcome to the WGUPS package delivery system.")
    print("How may we assist you today?")
    # Main menu loop - continues until user exits
    while True:
        print("\n--- Please select one of the following options: ---")
        print("1. Check status of a single package")
        print("2. Check status of all packages")
        print("3. View total mileage")
        print("4. Exit")

        # store user input in variable
        choice = input("\nEnter your choice here: ").strip()

        # Single package status:
            # gets singular package ID - validity check
            # gets exact time
            # looks up package ID in hashtable O(1)
            # Displays the status if there is one, else gives error response

        if choice == '1':
            try:
                pkg_id = int(input("Enter package ID (1-40): "))
                if pkg_id < 1 or pkg_id > 40:
                    print("Invalid package ID. Please enter a number between 1 and 40.")
                    continue

                hours = int(input("Enter hour (0-23): "))
                minutes = int(input("Enter minutes (0-59): "))
                check_time = timedelta(hours=hours, minutes=minutes)

                package = package_table.lookup(pkg_id)

                if package:
                    display_package_status(package, check_time)
                else:
                    print(f"Package {pkg_id} not found.")

            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        # Presents package statuses in three specific time ranges as required by rubric
            # user picks pre-curated time range - stored in variable
            # picked mid-points for my time for all ranges - easy to track
            # # Display packages organized by truck per rubric

        elif choice == '2':
            print("\nSelect a time range to check:")
            print("  A. Between 8:35 AM and 9:25 AM")
            print("  B. Between 9:35 AM and 10:25 AM")
            print("  C. Between 12:03 PM and 1:12 PM")

            time_choice = input("\nEnter your choice (A, B, or C): ").strip().upper()

            if time_choice == 'A':
                check_time = timedelta(hours=9, minutes=0)
                time_label = "9:00 AM (8:35 AM - 9:25 AM range)"
            elif time_choice == 'B':
                check_time = timedelta(hours=10, minutes=0)
                time_label = "10:00 AM (9:35 AM - 10:25 AM range)"
            elif time_choice == 'C':
                check_time = timedelta(hours=12, minutes=30)
                time_label = "12:30 PM (12:03 PM - 1:12 PM range)"
            else:
                print("Invalid choice. Please select A, B, or C.")
                continue

            print(f"\nSTATUS OF ALL PACKAGES AT {time_label}")

            print("\n--- TRUCK 1 PACKAGES ---")
            truck1_ids = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
            for pkg_id in truck1_ids:
                package = package_table.lookup(pkg_id)
                if package:
                    display_package_status(package, check_time)

            print("\n--- TRUCK 2 PACKAGES ---")
            truck2_ids = [3, 6, 18, 25, 28, 32, 36, 38, 2, 4, 5, 7, 8, 10]
            for pkg_id in truck2_ids:
                package = package_table.lookup(pkg_id)
                if package:
                    display_package_status(package, check_time)

            print("\n--- TRUCK 3 PACKAGES ---")
            truck3_ids = [9, 11, 12, 17, 19, 21, 22, 23, 24, 26, 27, 33, 35, 39]
            for pkg_id in truck3_ids:
                package = package_table.lookup(pkg_id)
                if package:
                    display_package_status(package, check_time)

        # displays total mileage by all trucks
        elif choice == '3':
            print(f"\nTotal mileage for all three trucks: {total_mileage:.2f} miles")
        # exits with goodbye message
        elif choice == '4':
            print("\nThank you for using WGUPS Package Tracking System!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")



def display_package_status(package, check_time):
    """
    Display detailed package information and status at a specified time.

    Determines package status by comparing check_time with departure_time
    and delivery_time.

    """

    # Determine package status based on time comparisons
    # Special handling for delayed packages (6, 25, 28, 32)
    # These don't arrive at hub until 9:05 AM - technically not at HUB
    delayed_packages = [6, 25, 28, 32]
    delayed_arrival = timedelta(hours=9, minutes=5)

    if package.package_id in delayed_packages and check_time < delayed_arrival:
        status = "Delayed on Flight"
        time_info = f"Arriving at hub at: {delayed_arrival}"

    elif package.delivery_time and check_time >= package.delivery_time:
        status = "Delivered"
        time_info = f"Delivered at: {package.delivery_time}"
    elif package.departure_time and check_time >= package.departure_time:
        status = "En Route"
        time_info = f"Departed at: {package.departure_time}"
    else:
        status = "At Hub"
        # Displays scheduled departure time if available
        time_info = f"Departs at: {package.departure_time if package.departure_time else 'Not scheduled'}"
    # Display package information with status/time info per rubric
    print(f"Package ID: {package.package_id}")
    print(f"Address: {package.address}, {package.city}, {package.state} {package.zipcode}")
    print(f"Deadline: {package.deadline}")
    print(f"Weight: {package.weight} kg")
    print(f"Status: {status}")
    print(f"{time_info}")
    print()


if __name__ == "__main__":
    main()

