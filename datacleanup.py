import csv
import regression
import math

#----------------------------------------------------------------
# Cleanup functions for state population file.

# Constants for our project
# Number of columns to take from the .csv file
numberOfCols = 11
# Increment of years in the .csv
increment = 10
# Starting and ending years of data
startYear = 1900
endYear = 1990
# Desired starting and ending year we want data for
desiredStartYear = 1984
desiredEndYear = 2015

# isInvalidRow: list -> bool
# Given a list row, isInvalidRow(row) will return true if the row does not contain
# usable data and false otherwise.
def isInvalidRow(row):
	return len(row) == 1 or row[0] == "" or row[1] == ""

# generateYears: int x int x int -> list
# Returns a list containing all the years in the range [fromYear, toYear]
# by increments specified (1 is the default).
def generateYears(fromYear, toYear, increment=1):
	years = []
	for i in range(fromYear, toYear + 1, increment):
		years.append(float(i))
	return years

# clean: list -> list
# Given a list in the following form: [<state_name>, data1, data2, ...]
# clean(row) will returns list which will reverse all the data values 
# but keep the state name at the front of the list. This is required since
# the data is given from most recent to least recent and the regression line
# should intuitively increase since population tends to grow over time.
def clean(row):
	len(row)
	r = []
	for i in range(0, len(row)):
		# First element should still be the state name.
		if i == 0:
			r.append(row[i])
		else:
			# Prepend all elements starting at index 1 to reverse and 
			# get rid of all commas within a number.
			r.insert(1, float(row[i].replace(",", "")))
	return r

# readData: int -> list of lists
# Returns a list of lists containing the information from "PopulationByState.csv"
# and ignoring any invalid rows.
def readData(numberOfCols):
	file = open("PopulationByState.csv", "r")
	reader = csv.reader(file)
	data = []
	for row in reader:
		# Skip invalid rows
		if isInvalidRow(row):
			continue
		else:
			# Store the first 'numberOfCols' columns of data
			row = row[:numberOfCols]
			# Clean the data (reverse and convert to floats)
			row = clean(row)
			# Append to the list of lists.
			data.append(row)
	file.close()
	return data

# printData: list -> void
# Prints out ever elements of a given list.
def printData(data):
	i = desiredStartYear
	for row in data:
		print("State: " + row[0])
		for j in range(1, len(row)):
			print(str(i) + ": " + str(row[j]))
			i += 1
		i = desiredStartYear


def modifyRow(row):
	rowWithoutState = row[1:]
	modifiedRow = [0 for x in range(desiredEndYear - desiredStartYear + 1)]
	years = generateYears(startYear, endYear, increment)

	regEqn = regression.getBestRegression(years, rowWithoutState)

	# Use regression to fill in the years in between
	# for example 1901, 1945, 1987.
	for i in range(0, desiredEndYear - desiredStartYear + 1):
		modifiedRow[i] = math.ceil(regEqn(desiredStartYear + i))
			
	# Insert the name of the state as the first element.
	modifiedRow.insert(0, row[0])
	return modifiedRow

def insertIntoData(data):
	modifiedData = []
	for row in data:
		modifiedRow = modifyRow(row)
		modifiedData.append(modifiedRow)
	return modifiedData


def getModifiedData():
	data = readData(numberOfCols)
	modifiedData = insertIntoData(data)
	return modifiedData



#---------------------------------------------------------------
# Cleanup functions for mortality rates file.

# cleanUpMortality: void -> list
# Returns a list of the valid rows taken from the mortality rates
# dataset.
def cleanUpMortality():
	file = open("Mortality Rates.csv", "r")
	reader = csv.reader(file)
	validRows = []
	validYears = [int(x) for x in range(1984, 2016)]

	# Trim out years not in 1984-2015
	for line in reader:
		if line[0] == "Year":
			validRows.append(line)
			continue
		if int(line[0]) not in validYears:
			continue
		if "" in line:
			continue
		if line[4] == "DC":
			continue
		else:
			validRows.append(line)

	# Trim out columns not going to be used
	validData = []
	for row in validRows:
		trimmedRow = []
		trimmedRow.append(row[0]) # Year
		trimmedRow.append(row[1]) # Week
		trimmedRow.append(row[3]) # Region
		trimmedRow.append(row[4]) # State
		trimmedRow.append(row[5]) # City
		trimmedRow.append(row[7]) # All Deaths
		trimmedRow.append(row[8]) # <1
		trimmedRow.append(row[9]) # 1-24
		trimmedRow.append(row[10]) # 25-44
		trimmedRow.append(row[11]) # 45-64
		trimmedRow.append(row[12]) # 65+
		validData.append(trimmedRow)

	combinedData = combineWeekData(validData)
	file.close()
	return combinedData

# combineWeekData: list of lists -> list of lists
# Returns a list of lists by combining data for a city
# for a given year. 
def combineWeekData(data):
	combinedData = []
	i = 0
	while(i < len(data)):
		if i == 0:
			combinedData.append(["Year", "Region", "State", "City", "All Deaths", 
				"< 1", "1-24", "25-44", "45-64", "65+"])
			i += 1
			continue
		currentCity = data[i][4]
		year = data[i][0]
		region = data[i][2]
		state = data[i][3]
		allDeaths = 0
		deaths_1 = 0
		deaths_1_to_24 = 0
		deaths_25_to_44 = 0
		deaths_45_to_64 = 0
		deaths_65 = 0
		while(i < len(data) and year == data[i][0]):
			allDeaths += int(data[i][5])
			deaths_1 += int(data[i][6])
			deaths_1_to_24 += int(data[i][7])
			deaths_25_to_44 += int(data[i][8])
			deaths_45_to_64 += int(data[i][9])
			deaths_65 += int(data[i][10])
			i += 1
		combinedRow = [year, region, state, currentCity, allDeaths, deaths_1, deaths_1_to_24,
							deaths_25_to_44, deaths_45_to_64, deaths_65]
		combinedData.append(combinedRow)
	return combinedData

#----------------------------------------------------------------
# Cleanup for the 
def cleanupIncome():
	file = open("MedianIncome.csv", "r")
	reader = csv.reader(file)
	for line in reader:
		print(line)



if __name__ == '__main__':
	data = getModifiedData()
	