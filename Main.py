import csv

from HashTable import HashTable


def main():
    packages = load_packages()
    address_list, distance_table = load_distance_table()

    print(get_distance(address_list, distance_table, '4001 South 700 East', '1060 Dalton Ave S'))

    # for i in range(1, 10):
    #     print(i, packages.get_value(i))

def load_packages():
    packages = HashTable()
    with open('Docs/WGUPS Package File.csv', mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            packages.set_value(int(line[0]), line[1:])

    return packages

def load_distance_table():
    address_list = HashTable()
    distance_table = []
    with open('Docs/WGUPS Distance Table.csv', mode='r') as file:
        csv_file = csv.reader(file)
        for i, line in enumerate(csv_file):
            address_list.set_value(line[0], i)
            distance_table.append(line[1:])

    return address_list, distance_table

def get_distance(address_list, distance_table, first_address, second_address):
    first_index = address_list.get_value(first_address)
    second_index = address_list.get_value(second_address)

    if distance_table[first_index][second_index]:
        return float(distance_table[first_index][second_index])
    else:
        return float(distance_table[second_index][first_index])



if __name__ == '__main__':
    main()