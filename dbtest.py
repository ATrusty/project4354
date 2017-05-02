import pyodbc
import csv


server = 'testdb4354.database.windows.net'
database = 'testdb'
username = ''
password = ''
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM TestTable")
rows = cursor.fetchall()
for row in rows:
	print(row)

cursor.close()
cnxn.close()