import csv
import psycopg2

connection = psycopg2.connect(
  database = "postgres",
  user = "postgres",
  host = "localhost",
  password = "password",
  port = 5433
)

def getFileName(file):
   sections = file.name.split("/")
   name = sections[-1].split(".")[0]
   return name

def createAndPopulateTable(file):
  with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for i in range(len(header)):
      header[i] = header[i].replace(" ", "_")
    columns = ','.join(header)

    file_name = getFileName(csv_file)
    cursor = connection.cursor()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {file_name}_olympics ({','.join([i + " varchar" for i in header])})""")
    print(f"""CREATE TABLE IF NOT EXISTS {file_name}_olympics ({','.join([i + " varchar" for i in header])})""")

    connection.commit()

    # for row in csv_reader:
    #     cursor.execute(f"INSERT INTO {file_name} VALUES ({row})")

    # connection.commit()
    cursor.close()

dictionary = './raw_data/dictionary.csv'
summer = './raw_data/summer.csv'
winter = './raw_data/winter.csv'

createAndPopulateTable(dictionary)
createAndPopulateTable(summer)
createAndPopulateTable(winter)

connection.close()