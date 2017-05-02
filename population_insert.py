import pyodbc
import csv


server = 'testdb4354.database.windows.net'
database = 'testdb'
username = 'kyao'
password = 'Database4354'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cursor = cnxn.cursor()

csv_data = csv.reader(open('populations.csv'))
for row in csv_data:
    startingYear = 1984
    for i in range (0, len(row)-1):
        year = startingYear + i
        state = row[0]
        population = row[1+i]
        cursor.execute("INSERT INTO Population(state_name, year, population_number) VALUES(?, ?, ?)", state, year, population)
        cursor.commit()
print("Done inserting")
        
