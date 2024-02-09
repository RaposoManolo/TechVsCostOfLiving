#import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import io
import requests
from dash import Dash, html, dcc, callback
import dash_bootstrap_components as dbc

columns = ["Country", "AvgSalary", "Cost of Living Index"]

#df = pd.read_csv("TechCostOfLiving.csv", index_col=2, usecols=columns)
url ="https://raw.githubusercontent.com/RaposoManolo/TechVsCostOfLiving/main/TechCostOfLiving.csv"
s=requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=2, usecols=columns)
#print(df)
df = df.rename(columns={'AvgSalary': 'Avg Salary - Thousands (USD)'})

## Web App Layout
app = Dash(title="Tech Salaries",
    external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    children=[
        html.H1("Avg Tech Salary Vs Cost of Living", style={"text-align": "center"}),
        html.Br(),
          html.Div(
            children=[
                    dcc.Graph(id="scatter_chart", figure=px.scatter(df, x="Avg Salary - Thousands (USD)", y="Cost of Living Index", text="Country", log_x=True, size_max=100))
            ],
            style={"display": "center", "width": "100%", "height": "90%"}
        ),
    ],
    style={"padding": "0px"}
)



#fig.update_traces(textposition='top center')
#fig.update_layout(title_text='Avg Tech Wage Vs Cost of Living', title_x=0.5)
#fig.show()

if __name__ == "__main__":
    app.run_server(debug=True)