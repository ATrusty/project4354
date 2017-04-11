import csv
import regression

numberOfCols = 11
increment = 10
startYear = 1900
endYear = 1990

# isInvalidRow: list -> bool
# Given a list row, isInvalidRow(row) will return true if the row does not contain
# usable data and false otherwise.
def isInvalidRow(row):
	return len(row) == 1 or row[0] == "" or row[1] == ""

def generateYears(fromYear, toYear, increment=1):
	years = []
	for i in range(fromYear, toYear + 1, increment):
		years.append(float(i))
	return years

def clean(row):
	len(row)
	r = []
	for i in range(0, len(row)):
		if i == 0:
			r.append(row[i])
		else:
			r.insert(1, float(row[i].replace(",", "")))
	return r

def readData(numberOfCols):
	file = open("PopulationByState.csv", "r")
	reader = csv.reader(file)
	data = []
	for row in reader:
		if isInvalidRow(row):
			continue
		else:
			row = row[:numberOfCols]
			row = clean(row)
			data.append(row)
	return data

def printData(data):
	for row in data:
		print(row)

def modifyRow(row):
	modifiedRow = [0 for x in range(91)]
	# Put data from csv rows in appropriate place
	for i in range(0, len(row)):
		modifiedRow[i * 10] = row[i]

	# Use linear regression to fill in the years in between
	# for example 1901, 1945, 1987.
	for i in range(0, len(modifiedRow)):
		# Skip calculating population for years already given
		if i % 10 == 0:
			continue
		# Use regression for a year we don't have
		else:
			years = generateYears(startYear, endYear, increment)
			regressionEquation = regression.getRegressionEquation(years, row[1:])

	print(modifiedRow)

def insertData(data):
	modifiedData = []
	for row in data:
		modifiedRow = modifyRow(row)

def getData():
	data = readData(numberOfCols)
	modifiedData = insertData(data)
	file.close()
	return data


if __name__ == '__main__':
	data = getData()
	printData(data)
	main()
