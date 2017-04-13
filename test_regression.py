import datacleanup
import regression
import math
rows = datacleanup.readData(11)
years = datacleanup.generateYears(1900, 1990, 10)

# Values taken from Excel and plugged into Wolfram Alpha.
def test_getLinRegEqn_1900to1990_US_1985():
	# US is the first row
	regEqn = regression.getLinRegEqn(years, rows[0][1:])
	assert abs(regEqn(1985) - 2.3065035797999954*10**8) < 10

def test_getLinRegEqn_1900to1990_Maine_1950():
	# Maine is the 20th row
	regEqn = regression.getLinRegEqn(years, rows[20][1:])
	assert abs(regEqn(1950) - 935533.939393) < .01

def test_getLinRegEqn_1900to1990_Texas_1968():
	# Texas is the 44th row
	regEqn = regression.getLinRegEqn(years, rows[44][1:])
	assert abs(regEqn(1968) - 1.1742374879999995*10**7) < 10

def test_getExpRegCoeffBase_WebExample():
	xVals = [0, 2, 4, 7]
	yVals = [3, 4, 11, 25]
	tup = regression.getExpRegCoeffBase(xVals, yVals)
	assert abs(tup[0] - 2.6770) < .1

def test_getExpRegEqn_WebExample():
	xVals = [0, 2, 4, 7]
	yVals = [3, 4, 11, 25]
	eqn = regression.getExpRegEqn(xVals, yVals)
	assert (eqn(20) - 1620.317) < 1
	# def test_modifyRow_UnitedStates_2015():
	# 	return

def test_getExpRegCoeffBase_1900to1990_US_2015():
	tup = regression.getExpRegCoeffBase(years, rows[0][1:])
	assert abs(tup[0] - .0015) < .0001
	assert abs(tup[1] - 1.01308) < .0001

def test_getExpRegCoeffBase_1900to1990_WY_1965():
	tup = regression.getExpRegCoeffBase(years, rows[51][1:])
	assert abs(tup[0] - math.pow(7, -9)) < .0001
	assert abs(tup[1] - 1.016128) < .0001

def test_getExpRegEqnCoeffBase_1900to1990_MN():
	tup = regression.getExpRegCoeffBase(years, rows[24][1:])
	assert abs(tup[0] - .0145) < .001
	assert abs(tup[1] - 1.00984) < .001

def test_getExpRegEqn_1900to1990_US_2015():
	eqn = regression.getExpRegEqn(years, rows[0][1:])
	# Within .1% of excel value
	assert abs(eqn(2015) - 3.5714714008*10**8) < 1

def test_getExpRegEqn_1900to1990_Texas_1966():
	eqn = regression.getExpRegEqn(years, rows[44][1:])
	tup = regression.getExpRegCoeffBase(years, rows[44][1:])
	print(tup[0])
	print(tup[1])
	assert abs(eqn(1966) - 1.0732906*10**7) < 1

def test_getExpRegEqn_WebExample2():
	eqn = regression.getExpRegEqn([0,1,2,3], [1,2,4,16])
	assert abs(eqn(5) - 78.8011) < .01

def test_getCoeffOfDeter_1900to1990_US():
	rSquared = regression.getCoeffOfDeter(years, rows[0][1:])
	logYVals = [math.log10(y) for y in rows[0][1:]]
	rExpSquared = regression.getCoeffOfDeter(years, logYVals)
	assert abs(rSquared - .9832) < .0001
	assert abs(rExpSquared - .9945) < .0001

def test_getCoeffOfDeter_1900to1990_MN():
	rSquared = regression.getCoeffOfDeter(years, rows[24][1:])
	logYVals = [math.log10(y) for y in rows[24][1:]]
	rExpSquared = regression.getCoeffOfDeter(years, logYVals)
	assert abs(rSquared - .9907) < .0001
	assert abs(rExpSquared - .9881) < .0001
