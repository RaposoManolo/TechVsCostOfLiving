import pandas as pd
import plotly.express as px
import io
import requests
from dash import Dash, html, dcc, callback
import dash_bootstrap_components as dbc

#Set variables
columns = ["Country", "AvgSalary", "Cost of Living Index"]
url ="https://raw.githubusercontent.com/RaposoManolo/TechVsCostOfLiving/main/TechCostOfLiving.csv"
s=requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=2, usecols=columns)
df = df.rename(columns={'AvgSalary': 'Avg Salary - Thousands (USD)'})
df = df.apply(lambda x: pd.Series(x.dropna().values)) ###
numberCountriesInScope= len(df["Country"])

## Web App Set
app = Dash(title="Tech Salaries", 
           external_stylesheets=[dbc.themes.DARKLY])

## Layout Set
app.layout = html.Div(
    children=[
        html.H1("Avg Tech Salary Vs Cost of Living", style={"text-align": "center"}),
        html.Div([dcc.Dropdown(options=[{'label': color, 'value': color}
                                       for color in ['blue', 'green', 'yello']])]),
        html.Br(),
        html.Div(
            dbc.Tabs([
                dbc.Tab([  
                        html.Br(),
                        html.Div(
                            children=[dcc.Graph(
                                id="scatter_chart", 
                                figure=px.scatter(df, x="Avg Salary - Thousands (USD)", y="Cost of Living Index", text="Country", log_x=True, size_max=100))
                            ], style={"display": "center", "width": "100%", "height": "100%"}
                            ),
                        ], style={"padding": "0px"}
                        ,label='Chart Analysis'),
                dbc.Tab([
                    html.Ul([
                        html.Br(),
                        html.Li('Author: Iuri Manuel Raposo'),
                        html.Li(['GitHub repo: ',
                        html.A('https://github.com/RaposoManolo/TechVsCostOfLiving/',
                                href='https://github.com/RaposoManolo/TechVsCostOfLiving/')
                                ]),
                        html.Li(['# of countries in scope: '] + [numberCountriesInScope]),
                        html.Li([
                            'Data Source: ',
                                html.A('https://www.numbeo.com/cost-of-living/region_prices_by_city?itemId=105&region=150',
                                href='https://www.numbeo.com/cost-of-living/region_prices_by_city?itemId=105&region=150')
                                ]) ,
                        html.Li('Update Frequency: To be set'),
                        html.Li('Last Updated:2024 Q1'),
                        html.Li('Goal: Testing the capabilities of Python using the Plotly and Dash framework.'),           
                            ])
                        ], label='Project Info')
            ]),
           
        ),
    ],style={"padding": "0px"}
)

if __name__ == "__main__":
    app.run_server(debug=False)