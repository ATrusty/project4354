import pyodbc
import csv


server = 'testdb4354.database.windows.net'
database = 'testdb'
username = 'kyao'
password = 'Database4354'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cursor = cnxn.cursor()

csv_data = csv.reader(open('StatesTable.csv'))
statesDict = {	"AL": "Alabama", 
		"AK": "Alaska", 
    		"AZ": "Arizona", 
					"AR": "Arkansas",
					"CA": "California",
					"CO": "Colorado",
					"CT": "Connecticut",
					"DE": "Delaware",
					"FL": "Florida",
					"GA": "Georgia",
					"HI": "Hawaii",
					"ID": "Idaho",
					"IL": "Illinois",
					"IN": "Indiana",
					"IA": "Iowa",
					"KS": "Kansas",
					"KY": "Kentucky",
					"LA": "Louisiana",
					"ME": "Maine",
					"MD": "Maryland",
					"MA": "Massachusetts",
					"MI": "Michigan",
					"MN": "Minnesota",
					"MS": "Mississippi",
					"MO": "Missouri",
					"MT": "Montana", 
					"NE": "Nebraska",
					"NV": "Nevada",
					"NH": "New Hampshire",
					"NJ": "New Jersey",
					"NM": "New Mexico",
					"NY": "New York",
					"NC": "North Carolina",
					"ND": "North Dakota",
					"OH": "Ohio",
					"OK": "Oklahoma",
					"OR": "Oregon",
					"PA": "Pennsylvania",
					"RI": "Rhone Island",
					"SC": "South Carolina",
					"SD": "South Dakota",
					"TN": "Tennessee",
					"TX": "Texas",
					"UT": "Utah",
					"VT": "Vermont",
					"VA": "Virginia",
					"WA": "Washington",
					"WV": "West Virginia",
					"WI": "Wisconsin",
					"WY": "Wyoming",
					}
for row in csv_data:
    cursor.execute("INSERT INTO StatesTable_temp(state_name, region) \
                    VALUES(?, ?)", statesDict[row[0]], row[1])
    print ("working")
#close the connection to the database.
cursor.commit()
cursor.close()
print ("Done")
