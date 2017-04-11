import pyodbc
import csv


server = 'cs4354.database.windows.net'
database = 'cs4354db'
username = ''
password = ''
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cursor = cnxn.cursor()


cursor.close()
cnxn.close()