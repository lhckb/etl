import csv
from sqlalchemy.orm import sessionmaker
from models import createTables, engine, DictionaryOlympics

createTables()

dictionary = './raw_data/dictionary.csv'
summer = './raw_data/summer.csv'
winter = './raw_data/winter.csv'

with open(dictionary, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    Session = sessionmaker(bind = engine)
    sessionobj = Session()

    for row in csv_reader:
        row[2] = int(row[2]) if len(row[2]) > 0 else 0
        row[3] = float(row[3]) if len(row[3]) > 0 else 0

        sessionobj.merge(DictionaryOlympics(
            country = row[0], 
            code = row[1], 
            population = int(row[2]), 
            gdp_per_capita = float(row[3])
          ))

    sessionobj.commit()
    sessionobj.close()