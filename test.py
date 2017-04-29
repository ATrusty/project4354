import pyodbc
import csv


def main():
    server = 'testdb4354.database.windows.net'
    database = 'testdb'
    username = 'kyao'
    password = 'Database4354'
    driver= '{ODBC Driver 13 for SQL Server}'
    cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
    cursor = cnxn.cursor()

    file = open("top10citiesMortality.csv", "w", newline='')

    cursor.execute("select city, state_name, death from CityMortality "
                   "where death IN (select MAX(death) from CityMortality "
                   "where year = 1984 group by state_name) order by death DESC")

    cityMortality = cursor.fetchall()

    top10 = []
    for i in range(0, 10):
        top10.append(cityMortality[i])

    writer = csv.writer(file)
    header = ["city", "state", "death"]
    writer.writerow(header)
    
    for row in top10:
        state = row[1]
        
        writer.writerow(row)
    file.close()
