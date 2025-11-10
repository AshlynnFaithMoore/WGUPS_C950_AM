import csv
from Package import Package

def clean_address(address):
    """
    This function standardizes all addresses to ensure
    consistent matching when calculating distances and to reduce bugs.

    Does so by replacing newline with spaces, abbreviating directions, and removing zip code parenthesis
    """

    # replace parenthesis
    if '(' in address:
        address = address.split('(')[0].strip()

    # Replace newlines with spaces
    address = address.replace('\n', ' ').strip()

    # Standardize with directional abbreviations
    replacements = {
        ' South ': ' S ',
        ' North ': ' N ',
        ' East ': ' E ',
        ' West ': ' W ',
    }

    # Apply each replacement
    for old, new in replacements.items():
        address = address.replace(old, new)

    return address

def read_package_file(filename, p_hash):
    """
    This function reads the package file

    """
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:

            # print for debugging purposes
            print(row)

            package_id = int(row[0])  # Convert to integer for consistency
            address = clean_address(row[1])  # Normalize address format - fixes previous bug
            city = row[2].strip()
            state = row[3].strip()
            zipcode = row[4].strip()
            deadline = row[5].strip()
            weight = row[6].strip()
            package = Package(package_id, address, city, state, zipcode, deadline, weight) #unpack row
            p_hash.insert(package.package_id, package)
            print(f"Loaded package {package_id}: {address}")#package id is the key, the rest is the value (object)

def read_distance_file(filename):
    """
    This function reads the distance file

    """
    distances = []
    addresses = []
    with open(filename, "r", encoding = "utf-8-sig") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        for row in reader:
            address = clean_address(row[1])
            addresses.append(address)
            # print for debugging purposes
            print(row)
            row_distances = []

            for x in row[2:]:  # skip first two columns - not needed
                if x == '':
                    row_distances.append(0.0)
                else:
                    row_distances.append(float(x))

            # add to main row to make a 2-D matrix
            distances.append(row_distances)
      # Return both the distance matrix and corresponding addresses
        return distances, addresses



