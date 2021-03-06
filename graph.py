import plotly as plot
import pandas as pd
import csv
import pyodbc
import plotly.graph_objs as go


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

def graphAverageMedianIncome():
    df = pd.read_csv("incomeFrom1984to2012.csv")
    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [[0.0, 'rgb(235,239,255)'],[0.2, 'rgb(184,200,255)'],[0.4, 'rgb(133,161,255)'],\
                [0.6, 'rgb(82,122,255)'],[0.8, 'rgb(0,49,209)'],[1.0, 'rgb(0,37,158)']]

    df['text'] = df['state']

    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = df['code'],
            z = df['avg_income'].astype(float),
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            colorbar = dict(
                title = "Avg. Med Income")
            ) ]

    layout = dict(
            title = '<b>Average Median Income by State</b>' + "<br>" + "<b>1984-2012</b>",
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                 )
        
    fig = dict( data=data, layout=layout )
    plot.offline.plot( fig, filename='avgMedianIncomes.html' )

def graphProportionLessThanOne():
    df = pd.read_csv("mapProportionLessThan1.csv")
    for col in df.columns:
        df[col] = df[col].astype(str)

        scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
                [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

    df['text'] = df['state']

    data = [ dict(
            type='choropleth',
            colorscale = 'Reds',
            autocolorscale = True,
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
            title = '<b>Proportion of deaths age < 1 to state population</b>' + "<br>" + "<b>1984-2012</b>",
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                 )
        
    fig = dict( data=data, layout=layout )
    plot.offline.plot( fig, filename='lessThanOneGraph.html' )

def graphProportionMiddleAge():
    df = pd.read_csv("proportionMiddleAge.csv")
    for col in df.columns:
        df[col] = df[col].astype(str)

        scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
                [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

    df['text'] = df['state']

    data = [ dict(
            type='choropleth',
            colorscale = 'Reds',
            autocolorscale = True,
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
            title = '<b>Proportion of deaths age 25-44 to state population</b>' + "<br>" + "<b>1984-2012</b>",
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                 )
        
    fig = dict( data=data, layout=layout )
    plot.offline.plot( fig, filename='middleAgeGraph.html' )


def graphProportionOver65():
    df = pd.read_csv("proportionOver65.csv")
    for col in df.columns:
        df[col] = df[col].astype(str)

        scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
                [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

    df['text'] = df['state']

    data = [ dict(
            type='choropleth',
            colorscale = 'Reds',
            autocolorscale = True,
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
            title = '<b>Proportion of deaths age 65+ to state population</b>' + "<br>" + "<b>1984-2012</b>",
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                 )
        
    fig = dict( data=data, layout=layout )
    plot.offline.plot( fig, filename='over65Graph.html' )

def graphTop10Mortality1984():
    df = pd.read_csv('top20citiesMortality1984.csv')
    
    data = [go.Bar(
            x=df['city'],
            y=df['death']
    )]

    layout = go.Layout(
        title="<b>Top 10 City Mortality Rates in 1984</b>",
        xaxis=dict(
            title="<b>City</b>"
        ),

        yaxis=dict(
            title="<b>Mortalities</b>"
        )
    )

    figure=go.Figure(data=data,layout=layout)

    plot.offline.plot(figure, filename='Top 20 cities with highest deaths in 1984.html')

def graphTop10Mortality2000():
    df = pd.read_csv('top20citiesMortality2000.csv')
    
    data = [go.Bar(
            x=df['city'],
            y=df['death']
    )]

    layout = go.Layout(
        title="<b>Top 10 City Mortality Rates in 2000</b>",
        xaxis=dict(
            title="<b>City</b>"
        ),

        yaxis=dict(
            title="<b>Mortalities</b>"
        )
    )

    figure=go.Figure(data=data,layout=layout)

    plot.offline.plot(figure, filename='Top 20 cities with highest deaths in 2000.html')

def graphTop10Mortality2012():
    df = pd.read_csv('top20citiesMortality2012.csv')
    
    data = [go.Bar(
            x=df['city'],
            y=df['death']
    )]

    layout = go.Layout(
        title="<b>Top 10 City Mortality Rates in 2012</b>",
        xaxis=dict(
            title="<b>City</b>"
        ),

        yaxis=dict(
            title="<b>Mortalities</b>"
        )
    )

    figure=go.Figure(data=data,layout=layout)

    plot.offline.plot(figure, filename='Top 20 cities with highest deaths in 2012.html')


def main():
    graphProportionLessThanOne()
    graphProportionMiddleAge()
    graphProportionOver65()
    graphAverageMedianIncome()
    graphTop10Mortality1984()
    graphTop10Mortality2000()
    graphTop10Mortality2012()



main()
