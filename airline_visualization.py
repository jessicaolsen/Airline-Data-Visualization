#Import Required Packages
import pandas as pd 
import plotly.express as px 
import dash 
from dash import html
from dash import dcc

#Read the airline data into Panda Dataframe
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                            encoding = "ISO-8859-1", 
                            dtype = {'DivlAirport': str, 'DivlTailNum' : str, 'Div2Airport': str, 'Div2TailNum': str})

#Randomly sample 500 data points
data = airline_data.sample(n= 500, random_state = 42)

#Creating a pie chart
fig = px.pie(data, values = 'Flights', names = 'DistanceGroup', title = 'Distance group proportion by flights')

#Create a dash application
app = dash.Dash(__name__)
#Update layout of application- Add Outer Division, Add Title, Add description to graph
app.layout = html.Div(children = [html.H1('Airline Dashboard', style = {'textAlign' : 'center', 'color': '#503D36', 'font-size': 40}), html.P('Proportion of distance group(250 mile distance interval group) by flights.', style = {'textAlign': 'center', 'color': '#F57241'}), dcc.Graph(figure = fig)])
if __name__ == '__main__': 
    app.run_server()
