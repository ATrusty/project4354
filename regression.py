def getRegressionEquation(xVals, yVals):
	print(yVals)
	print(xVals)
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

	return lambda x: intercept + slope * x

