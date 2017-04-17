# This script is used to write the data we are going to use 
# to files before we insert them into a database.

import datacleanup

def main():
	statePopFile = open("populations.txt", "r")
	mortalityFile = open("mortality.txt", "w")
	data = datacleanup.getModifiedData()
	for line in statePopFile:
		d = line.rstrip(' \t\r\n\0').split(",")
		print(d)
	print(len(data[0]))
	# for row in data:
	# 	for element in row[0:-1]:
	# 		statePopFile.write(str(element) + ",")
	# 	statePopFile.write(str(row[-1]))
	# 	statePopFile.write("\n")


	statePopFile.close()

main()