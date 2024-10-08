# Student ID: 011808943
# C950 - Data Structures and Algorithms II

import csv
from datetime import datetime

from HashTable import HashTable


def main():
    packages = load_packages()
    address_table, distance_table = load_distance_table()
    truck1 = [1, 2, 4, 7, 13, 14, 15, 16, 19, 20, 21, 29, 33, 34, 39, 40]
    truck2 = [3, 5, 8, 10, 11, 12, 18, 23, 30, 36, 37, 38]
    truck3 = [6, 17, 22, 24, 25, 26, 28, 31, 32]

    print(get_distance(address_table, distance_table, '4001 South 700 East', '1060 Dalton Ave S'))

    for i in range(1, 10):
        print(i, packages.get_value(i))

    print(get_delivery_status(packages, 6, '10:00')[0].strftime('%H:%M'))

# Deliver the packages of a given truck
# Returns ending time and total distance of the truck
def deliver_packages(truck, start_time, packages, address_table, distance_table):
    current_time = start_time
    total_distance = 0



    return current_time, total_distance

# Get the delivery status of a given package at a given time
# First find the package, then its status history
# Iterate through history, finding the most recent one to the given time
def get_delivery_status(packages, package_id, time_str):
    package = packages.get_value(package_id)
    status_history = package[-1]

    input_time = datetime.strptime(time_str, '%H:%M')

    previous_status = status_history[0]
    for status_time, status in status_history:
        if input_time < status_time:
            return previous_status
        previous_status = status_time, status

    return previous_status

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

# Read csv file and add each package to packages HashTable
# The package ID will be the key, and it is the first number on each line
# Initialize the status history, with some exceptions for certain packages
# Accessing package details will be O(1) time
def load_packages():
    packages = HashTable()
    with open('Docs/WGUPS Package File.csv', mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            package_id = int(line[0])
            package_details = line[1:]

            if package_id in {6, 25, 28, 32}:
                status_time = datetime.strptime('09:05', '%H:%M')
            else:
                status_time = datetime.strptime('08:00', '%H:%M')

            package_details.append([(status_time, 'At the hub')])
            packages.set_value(package_id, package_details)

    return packages

# Read csv file and add distances to 2D matrix distance table
# Create an address HashTable so that addresses can be indexed, allowing easy access
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

if __name__ == '__main__':
    main()