import math

def getLinRegSlopIntercept(xVals, yVals):
	ymean = sum(yVals) / (len(yVals))
	xmean = sum(xVals) / len(xVals)
	slope = 0
	intercept = 0
	numerator = 0
	denominator = 0
	for i in range (0, len(xVals)):
		xDiff = xVals[i] - xmean
		yDiff = yVals[i] - ymean
		numerator += xDiff * yDiff
		denominator += xDiff ** 2

	slope = numerator / denominator
	intercept = ymean - slope * xmean
	return (slope, intercept)

def getLinRegEqn(xVals, yVals):
	slopeInterceptTuple = getLinRegSlopIntercept(xVals, yVals)
	return lambda x: slopeInterceptTuple[1] + slopeInterceptTuple[0] * x

def getExpRegCoeffBase(xVals, yVals):
	log_yVals = [math.log10(y) for y in yVals]
	slopeInterceptTuple = getLinRegSlopIntercept(xVals, log_yVals)
	r = math.pow(10, slopeInterceptTuple[0])
	A = math.pow(10, slopeInterceptTuple[1])
	return (A, r)

def getExpRegEqn(xVals, yVals):
	# Exponential function of the form y = Ar^x
	coeffBaseTuple = getExpRegCoeffBase(xVals, yVals)
	return lambda x: coeffBaseTuple[0]*math.pow(coeffBaseTuple[1], x)

def getCoeffOfDeter(xVals, yVals):
	n = len(xVals)
	sumX = sum(xVals)
	sumY = sum(yVals)
	sumOfProdXY = 0
	sumXSquared = 0
	sumYSquared = 0
	for i in range(0, len(xVals)):
		sumOfProdXY += xVals[i] * yVals[i]
		sumXSquared += math.pow(xVals[i], 2)
		sumYSquared += math.pow(yVals[i], 2)

	numerator = n * sumOfProdXY - float(sumX * sumY)
	denomLeftTerm = n * sumXSquared - math.pow(sumX, 2)
	denomRightTerm = n * sumYSquared - math.pow(sumY, 2)
	denominator = denomLeftTerm * denomRightTerm
	return math.pow(numerator / math.sqrt(denominator), 2)

def getBestRegression(xVals, yVals):
	# Calculate r^2 for both exponential regression and linear regression
	linCoeffDeter = getCoeffOfDeter(xVals, yVals)
	logYVals = [math.log10(y) for y in yVals]
	expCoeffDeter = getCoeffOfDeter(xVals, logYVals)
	regEqn = lambda x: x

	# If exponential r^2 > linear r^2 set equation to exponential regression
	if(expCoeffDeter > linCoeffDeter):
		regEqn = getExpRegEqn(xVals, yVals)
	# Otherwise set equation to linear regression
	else:
		regEqn = getLinRegEqn(xVals, yVals)
	return regEqn


