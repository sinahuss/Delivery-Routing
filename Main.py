import csv

from HashTable import HashTable


def main():
    table = HashTable()
    # package = (89234, ['address', 'deadline', 'city', 'zip code', 'weight', 'status'])
    #
    # table.set_value(package[0], package[1])
    #
    # print(package[0], table.get_value(package[0]))

    import_files(table)

def import_files(table: HashTable):
    with open('Docs/WGUPS Package File.csv', mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            print(line[0], line[1:])



if __name__ == '__main__':
    main()