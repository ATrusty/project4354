from sklearn import linear_model
import csv
import regression
import pyodbc
import math
import plotly
import plotly.graph_objs as go

model = linear_model.LinearRegression()

server = 'testdb4354.database.windows.net'
database = 'testdb'
username = 'admin1'
password = 'College22'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cursor = cnxn.cursor()
firstGivenYear = 1984
lastGivenYear = 2012
dbYears = [x for x in range(firstGivenYear, lastGivenYear + 1)]

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

predictStates = ["Tennessee", "Connecticut", "Ohio", "Oregon", "Oklahoma",
                 "Colorado", "Nebraska", "Texas", "North Carolina", "Washington"]

def main():
    # Get data into dictionary of xvars and yvalues
    dataSets = getDataSets()
    # Generate predictions up to a given year
    predictions = generatePredictions(dataSets, 2020)
    print(predictions)
    
    # Generate x-y values to plot on line graph
    XYValues = []
    for state in predictStates:
        print(state)
        valuesTuple = getXY(state, predictions)
        print(valuesTuple)
        XYValues.append(valuesTuple)
    
    # Graph XYValues for states we want predictions for
    graph(predictStates, XYValues)
   

    cursor.close()
    cnxn.close()

def getDataSets():
    infoFile = open("predictInfo.csv", "r")
    reader = csv.reader(infoFile)
    
    stateInfo = dict()
    for k, v in statesDict.items():
        stateInfo[v] = [[], []]
    

    for row in reader:
        xi = row[1:5]
        for i in range(0, len(xi)):
            xi[i] = int(xi[i])

        yi = int(row[-1])
        stateInfo[row[0]][0].append(xi)
        stateInfo[row[0]][1].append(yi)
    
    infoFile.close()
    return stateInfo

def generatePredictions(dataSets, year):
    for state in predictStates:
        # Fit the model based on the x and y values of a given state 
        # Only train on 80 percent of data
        model.fit(dataSets[state][0][0:22], dataSets[state][1][0:22])
        dataSets[state][0] = dataSets[state][0][0:22]
        dataSets[state][1] = dataSets[state][1][0:22]
        for i in range(firstGivenYear + 22, year + 1):
            income = predictIncome(state, i)
            pop = predictPopulation(state, i)
            region = getRegion(state)
            x = [i, income, pop, region]
            prediction = model.predict([x])
            dataSets[state][0].append(x)
            dataSets[state][1].append(math.ceil(prediction[0]))
    return dataSets


def predictIncome(state, year):
    cursor.execute("select median_income from PopulationIncome "
                   "where state_name = ? order by year", state)
    rows = cursor.fetchall()
    
    incomes = []
    for row in rows:
        incomes.append(int(row[0]))
    
    incomeEqn = regression.getLinRegEqn(dbYears, incomes)
#    print("Income: ")
#    print(incomes)
#    print(incomeEqn(year))
    return math.ceil(incomeEqn(year))
    
def predictPopulation(state, year):
    cursor.execute("select population from PopulationIncome "
                   "where state_name = ? order by year", state)
    rows = cursor.fetchall()
    
    pops = []
    for row in rows:
        pops.append(int(row[0]))
        
    popEqn = regression.getBestRegression(dbYears, pops)
#    print("Population: ")
#    print(pops)
#    print(popEqn(year))
    return math.ceil(popEqn(year))

def getRegion(state):
    cursor.execute("select region from StatesTable "
                   "where state_name = ?", state)
    region = cursor.fetchone()
    
    return int(region[0])

def getPopulations(stateName):
    file = open("populations.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] == stateName:
            for i in range(1, len(row)):
                 row[i] = int(row[i])
            file.close()
            return row[1:]
    print("Could not find: " + stateName)
    file.close()
    return []

def getXY(state, predictions):
    xVals = []
    yVals = []
    for key in predictions:
        if key == state:
            for xvar in predictions[state][0]:
                xVals.append(xvar[0])
            yVals = predictions[state][1]
            return (xVals, yVals)
    print("Could not find state: " + state)
    return None

def graph(states, XYValues):
    traces = []
    for i in range(0, len(XYValues)):
        trace = go.Scatter(
                    x = XYValues[i][0],
                    y = XYValues[i][1],
                    mode = 'lines+markers',
                    name = states[i]
                )
        traces.append(trace)
    layout = dict(title = "<b>Mortality Predictions Through 2020</b>",
                  xaxis = dict(title = "<b>Year</b>"),
                  yaxis = dict(title = "<b>Mortalities</b>"))
    data = traces
    fig = dict(data = data, layout=layout)
    plotly.offline.plot(fig, filename='MortalityPrediction2020.html')
    
main()