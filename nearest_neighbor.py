

# This greedy algorithm selects the closest undelivered package at each step

def get_distance(distance_table , address_list, address1, address2):

    """

    Retrieves the distance between two addresses from the distance matrix.

    Algorithm:
    1. Find index of address1 in address_list
    2. Find index of address2 in address_list
    3. Check distance_table[i][j]
    4. If it's 0.0, check distance_table[j][i] instead
    5. Return the non-zero distance

    """
    first = address_list.index(address1)
    second = address_list.index(address2)
    if distance_table[first][second] != 0:
        distance = distance_table[first][second]
    else:
        distance = distance_table[second][first]
    return distance


def deliver_packages(truck, package_hash, distance_data, address_list):
    """
        Deliver all packages on a truck using the Nearest Neighbor algorithm.

    Algorithm:
    1. Start at nearest location
    2. While packages are on the truck, follow through with delivering the package with nearest distance (greedy approach)
    3. Return to hub when truck is empty

    Time Complexity: O(n²) where n = number of packages on truck
        Outer loop runs n times (once per package)
        Inner loop checks n packages, decreasing by 1 each iteration

    Space Complexity: O(1)
        Modifies truck.packages list in place
    """
    # base case - checks to make sure all packages are present in hashtable
    for i in range(1, 41):
        if package_hash.lookup(i) is None:
            print(f"Package {i} is missing from the hash table!")

    current_address = truck.address #truck starts at hub
    # Main delivery loop - continue until all packages delivered
    while truck.packages: #while true
        nearest_package = None
        shortest_distance = float('inf') #fixed bug: set to high number (originally 0)
        for package_id in truck.packages:
            package = package_hash.lookup(package_id)
            if package is None:
                print(f"Warning: Package {package_id} not found in hash table") # was using to debug
                continue

            # Calculate distance from current location to this package's address
            distance = get_distance(distance_data, address_list, current_address, package.address)
            # greedy - compare and update the shortest distance found
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_package = package

        if nearest_package is None:
            break  # nothing left to deliver - ensure there is a valid package

        # Update truck mileage and time based on travel distance
        truck.update_mileage(shortest_distance)
        current_address = nearest_package.address

        # Mark delivery with timestamp - print for debugging
        nearest_package.delivery_time = truck.time
        # Remove package from truck's cargo list
        truck.packages.remove(nearest_package.package_id)
        print(f"Delivered package {nearest_package.package_id} at {truck.time}")

    # After all deliveries complete, truck must return to hub
    # Calculate distance from last delivery location back to HUB
    return_distance = get_distance(distance_data, address_list, current_address, 'HUB')
    truck.update_mileage(return_distance)
    truck.address = 'HUB'
    # print status report
    print(f"Truck returned to HUB at {truck.time}")
    print(f"Total mileage for this truck: {truck.mileage:.2f} miles\n")



