import csv

from HashTable import HashTable


def main():
    packages = load_packages()
    address_table, distance_table = load_distance_table()

    print(get_distance(address_table, distance_table, '4001 South 700 East', '1060 Dalton Ave S'))

    # for i in range(1, 10):
    #     print(i, packages.get_value(i))

# Read csv file and add each package to packages HashTable
# The package ID will be the key, and it is the first number on each line
# Accessing package details will be O(1) time
def load_packages():
    packages = HashTable()
    with open('Docs/WGUPS Package File.csv', mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            packages.set_value(int(line[0]), line[1:])

    return packages

# Create an address HashTable so that addresses can be indexed, allowing easy access
# Distance table is a 2D matrix,
# Using address table makes accessing distance O(1) time
def load_distance_table():
    address_table = HashTable()
    distance_table = []
    with open('Docs/WGUPS Distance Table.csv', mode='r') as file:
        csv_file = csv.reader(file)
        for i, line in enumerate(csv_file):
            address_table.set_value(line[0], i)
            distance_table.append(line[1:])

    return address_table, distance_table

# Access index of both addresses from address table
# Distance from A to B is same as B to A, so if the distance is empty,
# swap the indexes and get the distance
def get_distance(address_table, distance_table, first_address, second_address):
    first_index = address_table.get_value(first_address)
    second_index = address_table.get_value(second_address)

    if distance_table[first_index][second_index]:
        return float(distance_table[first_index][second_index])
    else:
        return float(distance_table[second_index][first_index])



if __name__ == '__main__':
    main()