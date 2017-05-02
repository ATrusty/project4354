import pyodbc
import csv


server = 'testdb4354.database.windows.net'
database = 'testdb'
username = 'kyao'
password = 'Database4354'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cursor = cnxn.cursor()

csv_data = csv.reader(open('MedianIncome.csv'))
for row in csv_data:
    if row[0] == "State":
        continue
    startingYear = 2012
    print("Working")
    for i in range (0, len(row)-2):
        year = startingYear - i
        state = row[0]
        income = row[2+i]
        cursor.execute("INSERT INTO Income(state_name, year, median_income) VALUES(?, ?, ?)", state, year, income)
        cursor.commit()
print("Done inserting")
