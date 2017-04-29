import plotly as plot
import pandas as pd
import csv
import pyodbc

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

server = 'testdb4354.database.windows.net'
database = 'testdb'
username = 'admin1'
password = 'College22'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cursor = cnxn.cursor()

def writeProportionLessThanOne(cursor):
    cursor.execute("SELECT m.state_name, SUM(deaths) "
        "FROM Mortality m, StatesTable s "
        "WHERE m.state_name = s.state_name AND age_ID = 1 "
        "GROUP BY m.state_name ORDER BY m.state_name")

    deathsLessThan1 = cursor.fetchall()

    cursor.execute("SELECT m.state_name, SUM(deaths) "
        "FROM Mortality m GROUP BY m.state_name ORDER BY m.state_name")

    totalDeaths = cursor.fetchall()
    for row in deathsLessThan1:
        print(row)

    print("\n")
    for i in range(0, len(totalDeaths)):
        print(str(totalDeaths[i]) + str(deathsLessThan1[i]))

    proportionDeathsLessThan1 = []
    for i in range(0, len(totalDeaths)):
        state = totalDeaths[i][0]
        proportion = float(deathsLessThan1[i][1]) / float(totalDeaths[i][1])
        proportionDeathsLessThan1.append([state, proportion])

    for row in proportionDeathsLessThan1:
        print(row)

    file = open("mapProportionLessThan1.csv", "w", newline='')
    writer = csv.writer(file)
    header = ["code", "state", "proportion"]
    writer.writerow(header)
    for row in proportionDeathsLessThan1:
        state = row[0]
        for k, v in statesDict.items():
            if(v == state):
                row.insert(0, k)
        writer.writerow(row)
    file.close()

def graphProportionLessThanOne():
    df = pd.read_csv("mapProportionLessThan1.csv")
    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
                [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

    df['text'] = df['state']

    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = df['code'],
            z = df['proportion'].astype(float),
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            colorbar = dict(
                title = "Proportion")
            ) ]

    layout = dict(
            title = 'Proportion of deaths age < 1 to state population' + "<br>" + "1984-2012",
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                 )
        
    fig = dict( data=data, layout=layout )
    plot.offline.plot( fig, filename='d3-cloropleth-map' )

# datafile = pd.read_csv('https: