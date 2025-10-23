

# decides the order and timing of deliveries

def get_distance(distance_table , address_list, address1, address2):
    first = address_list.index(address1)
    second = address_list.index(address2)
    if distance_table[first][second] != 0:
        distance = distance_table[first][second]
    else:
        distance = distance_table[second][first]
    return distance


def deliver_packages(truck, package_hash, distance_data, address_list):
    # nearest neighbor algo.
    for i in range(1, 41):
        if package_hash.lookup(i) is None:
            print(f"Package {i} is missing from the hash table!")

    current_address = truck.address #truck starts at hub
    while truck.packages: #while true
        nearest_package = None
        shortest_distance = float('inf') #fixed bug: set to high number
        for package_id in truck.packages:
            package = package_hash.lookup(package_id)
            if package is None:
                print(f"Warning: Package {package_id} not found in hash table")
                continue
            distance = get_distance(distance_data, address_list, current_address, package.address)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_package = package

        if nearest_package is None:
            break  # nothing left to deliver

            # Update truck mileage and time
        truck.update_mileage(shortest_distance)
        current_address = nearest_package.address

        # Mark delivery
        nearest_package.delivery_time = truck.time
        truck.packages.remove(nearest_package.package_id)
        print(f"Delivered package {nearest_package.package_id} at {truck.time}")



