import datacleanup
import regression

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

# Values taken from Excel and plugged into Wolfram Alpha.
def test_getRegressionEquation_1900to1990_US_1985():
	rows = datacleanup.getData()
	# US is the first row
	regEqn = regression.getRegressionEquation(datacleanup.generateYears(1900, 1990, 10), rows[0][1:])
	assert abs(regEqn(1985) - 2.3065035797999954*10**8) < 10

def test_getRegressionEquation_1900to1990_Maine_1950():
	rows = datacleanup.getData()
	# Maine is the 20th row
	regEqn = regression.getRegressionEquation(datacleanup.generateYears(1900, 1990, 10), rows[20][1:])
	assert abs(regEqn(1950) - 935538) < 10

def test_getRegressionEquation_1900to1990_Texas_1968():
	rows = datacleanup.getData()
	# Texas is the 44th row
	regEqn = regression.getRegressionEquation(datacleanup.generateYears(1900, 1990, 10), rows[44][1:])
	assert abs(regEqn(1968) - 1.1742374879999995*10**7)