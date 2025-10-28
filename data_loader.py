import csv
from Package import Package

def clean_address(address):
    if '(' in address:
        address = address.split('(')[0].strip()

    # Replace newlines with spaces
    address = address.replace('\n', ' ').strip()

    # Standardize directional abbreviations
    replacements = {
        ' South ': ' S ',
        ' North ': ' N ',
        ' East ': ' E ',
        ' West ': ' W ',
    }

    for old, new in replacements.items():
        address = address.replace(old, new)

    return address

def read_package_file(filename, p_hash):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:


            print(row)

            package_id = int(row[0])  # Convert to integer for consistency
            address = clean_address(row[1])  # Normalize address format
            city = row[2].strip()
            state = row[3].strip()
            zipcode = row[4].strip()
            deadline = row[5].strip()  # Note: deadline comes before weight in CSV
            weight = row[6].strip()
            package = Package(package_id, address, city, state, zipcode, deadline, weight) #unpack row
            p_hash.insert(package.package_id, package)
            print(f"Loaded package {package_id}: {address}")#package id is the key, the rest is the value (object)

def read_distance_file(filename):
    distances = []
    addresses = []
    with open(filename, "r", encoding = "utf-8-sig") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        for row in reader:
            address = clean_address(row[1])
            addresses.append(address)

            print(row)
            row_distances = []

            for x in row[2:]:  # skip first two columns
                if x == '':
                    row_distances.append(0.0)
                else:
                    row_distances.append(float(x))

            # add to main row to make a 2-D matrix
            distances.append(row_distances)

        return distances, addresses



