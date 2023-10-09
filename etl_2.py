import csv

file_path = './raw_data/olympic_medals.csv'

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    for row in csv_reader:
        print(row)

    print(header)