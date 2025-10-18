import csv
from Package import Package

def read_package_file(filename, p_hash):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            package_id = row[0]
            address = row[1]
            deadline = row[2]
            city = row[3]
            zipcode = row[4]
            weight = row[5]
            notes = row[6]
            package = Package(package_id, address, deadline, city, zipcode, weight, notes) #unpack row
            p_hash.insert(package.package_id, package) #package id is the key, the rest is the value (object)

def read_distance_file(filename):
    distances = []
    addresses = []
    with open(filename, "r", encoding = "utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
            addresses.append(row[1])
            row_distances = []

            for x in row[2:]:  # skip first two columns
                if x == '':
                    row_distances.append(0.0)
                else:
                    row_distances.append(float(x))

            # add to main row to make a 2-D matrix
            distances.append(row_distances)

        return distances, addresses



