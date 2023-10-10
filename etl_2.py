import csv
import psycopg2

connection = psycopg2.connect(
  database = "postgres",
  user = "postgres",
  host = "0.0.0.0",
  password = "password",
  port = 5432
)

def getFileName(file):
   sections = file.name.split("/")
   name = sections[-1].split(".")[0]
   return name


dictionary = './raw_data/dictionary.csv'
summer = './raw_data/summer.csv'
winter = './raw_data/winter.csv'

with open(dictionary, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for i in range(len(header)):
        header[i] = header[i].replace(" ", "_")

    file_name = getFileName(csv_file)
    cursor = connection.cursor()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {file_name}_olympics (
                   country varchar(100),
                   code varchar(4),
                   population bigint,
                   gdp_per_capita float(25)
    )""")

    connection.commit()

    for row in csv_reader:
        
        row[2] = int(row[2]) if len(row[2]) > 0 else 0
        row[3] = float(row[3]) if len(row[3]) > 0 else 0
        print(f"INSERT INTO {file_name}_olympics (country, code, population, gdp_per_capita) VALUES ({row})".replace("[", "").replace("]", "").replace("\"", "\'"))
        cursor.execute(f"INSERT INTO {file_name}_olympics (country, code, population, gdp_per_capita) VALUES ({row})".replace("[", "").replace("]", "").replace("\"", "\'"))

    connection.commit()
    cursor.close()


connection.close()