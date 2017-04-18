# This script is used to write the data we are going to use 
# to files before we insert them into a database.

import datacleanup

def main():
	statePopFile = open("populations.csv", "w")
	mortalityFile = open("mortalitytrimmed.csv", "w")
	statePopData = datacleanup.getModifiedData()
	mortalityData = datacleanup.cleanUpMortality()

	# for line in statePopFile:
	# 	d = line.rstrip(' \t\r\n\0').split(",")
	# 	print(d)
	# print(len(statePopData[0]))
	for row in statePopData:
		for element in row[0:-1]:
			statePopFile.write(str(element) + ",")
		statePopFile.write(str(row[-1]))
		statePopFile.write("\n")

	for row in mortalityData:
		for element in row[0:-1]:
			mortalityFile.write(element + ",")
		mortalityFile.write(row[-1])
		mortalityFile.write("\n")

	statePopFile.close()
	mortalityFile.close()

main()