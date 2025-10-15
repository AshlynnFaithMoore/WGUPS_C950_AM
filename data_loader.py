import csv
from Package import Package

def read_package_file(self, filename, p_hash):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            package = Package(*row) #unpack row
            p_hash.insert(package.package_id, package) #package id is the key, the rest is the value (object)

def read_distance_file(filename):
    distances = []
    addresses = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
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



