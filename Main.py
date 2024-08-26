import csv

from HashTable import HashTable


def main():
    packages = load_packages()

    for i in range(1, 10):
        print(i, packages.get_value(i))

def load_packages():
    table = HashTable()
    with open('Docs/WGUPS Package File.csv', mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            table.set_value(int(line[0]), line[1:])

    return table

def load_distance_table():



if __name__ == '__main__':
    main()