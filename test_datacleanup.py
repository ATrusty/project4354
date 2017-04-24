import datacleanup
import regression

rows = datacleanup.readData(11)
years = datacleanup.generateYears(1900, 1990, 10)
cleanData = datacleanup.cleanUpMortality()
def test_isInvalidRow_EmptyRow_True():
	result = datacleanup.isInvalidRow(["", "", ""])
	assert result == True

def test_isInvalidRow_LengthOne_True():
	result = datacleanup.isInvalidRow(["hello"])
	assert result == True

def test_isInvalidRow_LengthNotOne_False():
	result = datacleanup.isInvalidRow(["hello", "world"])
	assert result == False

def test_isInvalidRow_LengthNotOneSecondRowEmpty_False():
	result = datacleanup.isInvalidRow(["hello", ""])
	assert result == True

def test_generateYears_1900_1990_10():
	result = datacleanup.generateYears(1900, 1990, 10)
	assert result[0] == 1900.0
	assert result[-1] == 1990.0

def test_generateYears_emptyInterval():
	result = datacleanup.generateYears(1990, 1980, 10)
	assert result == []

def test_generateYears_1990_2000_3():
	result = datacleanup.generateYears(1990, 2000, 3)
	assert result[0] == 1990.0
	assert result[-1] == 1999.0

#Test modify row
def test_modifyRow_Texas_1984_2015_1984():
	result = datacleanup.modifyRow(rows[44])
	assert abs(result[1] - 1.498329642154914728117*10**7) < 1

def test_modifyRow_Texas_19884_2015_1999():
	result = datacleanup.modifyRow(rows[44])
	assert abs(result[16] - 1.978559282436642619633*10**7) < 1

def test_modifyRow_Texas_1984_2015_2015():
	result = datacleanup.modifyRow(rows[44])
	assert abs(result[-1] - 2.661584198796377390129*10**7) < 1

def test_cleanUpMortality_Boston_1984():
	# Assert total deaths are correct
	assert cleanData[0][4] == 9526
	assert cleanData[0][5] == 432

def test_cleanUpMortality_Tacoma_2015():
	assert cleanData[len(cleanData)-1][4] == 7030
	assert cleanData[len(cleanData)-1][6] == 114
