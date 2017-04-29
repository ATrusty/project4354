# This script is used to write the data we are going to use 
# to files before we insert them into a database.

import datacleanup
import pyodbc
import csv
import math
statesDict = {  "AL": "Alabama", 
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
                "RI": "Rhode Island",
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
def main():
	server = 'testdb4354.database.windows.net'
	database = 'testdb'
	username = 'admin1'
	password = 'College22'
	driver= '{ODBC Driver 13 for SQL Server}'
	cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
	cursor = cnxn.cursor()


	# statePopFile = open("populations.csv", "w")
	# mortalityFile = open("mortalitytrimmed.csv", "w")
	# statePopData = datacleanup.getModifiedData()
	# mortalityData = datacleanup.cleanUpMortality()

	writeProportionLessThanOne(cursor)
	writeIncomeForStates(cursor)
	writeProportionMiddleAge(cursor)
	writeProportionOver65(cursor)
	# for row in statePopData:
	# 	for element in row[0:-1]:
	# 		statePopFile.write(str(element) + ",")
	# 	statePopFile.write(str(row[-1]))
	# 	statePopFile.write("\n")

	# for row in mortalityData:
	# 	for element in row[0:-1]:
	# 		mortalityFile.write(str(element) + ",")
	# 	mortalityFile.write(str(row[-1]))
	# 	mortalityFile.write("\n")

	# Close files
	# statePopFile.close()
	# mortalityFile.close()
	
	# Close database connections
	cursor.close()
	cnxn.close()



def writeProportionLessThanOne(cursor):
	file = open("mapProportionLessThan1.csv", "w", newline='')

	cursor.execute("SELECT m.state_name, SUM(deaths) "
		"FROM Mortality m, StatesTable s "
		"WHERE m.state_name = s.state_name AND age_ID = 1 "
		"GROUP BY m.state_name ORDER BY m.state_name")

	deathsLessThan1 = cursor.fetchall()

	cursor.execute("SELECT m.state_name, SUM(deaths) "
		"FROM Mortality m GROUP BY m.state_name ORDER BY m.state_name")

	totalDeaths = cursor.fetchall()

	proportionDeathsLessThan1 = []
	for i in range(0, len(totalDeaths)):
		state = totalDeaths[i][0]
		proportion = float(deathsLessThan1[i][1]) / float(totalDeaths[i][1])
		proportionDeathsLessThan1.append([state, proportion])

	writer = csv.writer(file)
	header = ["code", "state", "proportion"]
	writer.writerow(header)
	for row in proportionDeathsLessThan1:
		state = row[0]
		for k, v in statesDict.items():
			if(v == state):
				row.insert(0, k)
		writer.writerow(row)
	file.close()


def writeProportionMiddleAge(cursor):
	file = open("proportionMiddleAge.csv", "w", newline = '')

	cursor.execute("SELECT m.state_name, SUM(deaths) "
		"FROM Mortality m, StatesTable s "
		"WHERE m.state_name = s.state_name AND age_ID = 3 "
		"GROUP BY m.state_name ORDER BY m.state_name")

	deathsMiddleAge = cursor.fetchall()

	cursor.execute("SELECT m.state_name, SUM(deaths) "
		"FROM Mortality m GROUP BY m.state_name ORDER BY m.state_name")

	totalDeaths = cursor.fetchall()

	proportionDeathsMiddleAge = []
	for i in range(0, len(totalDeaths)):
		state = totalDeaths[i][0]
		proportion = float(deathsMiddleAge[i][1]) / float(totalDeaths[i][1])
		proportionDeathsMiddleAge.append([state, proportion])

	writer = csv.writer(file)
	header = ["code", "state", "proportion"]
	writer.writerow(header)
	for row in proportionDeathsMiddleAge:
		state = row[0]
		for k, v in statesDict.items():
			if(v == state):
				row.insert(0, k)
		writer.writerow(row)
	file.close()	


def writeProportionOver65(cursor):
	file = open("proportionOver65.csv", "w", newline = '')

	cursor.execute("SELECT m.state_name, SUM(deaths) "
		"FROM Mortality m, StatesTable s "
		"WHERE m.state_name = s.state_name AND age_ID = 5 "
		"GROUP BY m.state_name ORDER BY m.state_name")

	deathsOver65 = cursor.fetchall()

	cursor.execute("SELECT m.state_name, SUM(deaths) "
		"FROM Mortality m GROUP BY m.state_name ORDER BY m.state_name")

	totalDeaths = cursor.fetchall()

	proportionDeathsOver65 = []
	for i in range(0, len(totalDeaths)):
		state = totalDeaths[i][0]
		proportion = float(deathsOver65[i][1]) / float(totalDeaths[i][1])
		proportionDeathsOver65.append([state, proportion])

	writer = csv.writer(file)
	header = ["code", "state", "proportion"]
	writer.writerow(header)
	for row in proportionDeathsOver65:
		state = row[0]
		for k, v in statesDict.items():
			if(v == state):
				row.insert(0, k)
		writer.writerow(row)
	file.close()	

def writeIncomeForStates(cursor):
	file = open("incomeFrom1984to2012.csv", "w", newline = '')
	# Number of years we have data for
	numYears = 29.0

	# Select the sum of the median_income for each state
	cursor.execute("SELECT state_name, SUM(median_income) FROM PopulationIncome "
		"GROUP BY state_name ORDER BY state_name")
	# Store result from database into 'rows'
	rows = cursor.fetchall()
	
	writer = csv.writer(file)

	# Create and write the header 
	header = ["code", "state", "avg_income"]
	writer.writerow(header)

	for i in range(0, len(rows)):
		incomeRow = []
		state = rows[i][0]
		# Skip United States data
		if state == 'United States':
				continue

		# Look for state abbreviation in dictionary
		for k, v in statesDict.items():
			# If the state abbreviation is found crete the row to write to csv
			if v == state:
				incomeRow = [k, state, math.ceil(rows[i][1] / numYears)]

		# Write the row to the csv file
		writer.writerow(incomeRow)
	file.close()



main()