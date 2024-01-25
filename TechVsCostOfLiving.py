#import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
#import numpy as np

import dash
from dash import html
import dash_bootstrap_components as dbc

columns = ["Country", "AvgSalary", "Cost of Living Index"]




df = pd.read_csv("TechCostOfLiving.csv", index_col=2, usecols=columns)

#print(df)


df = df.rename(columns={'AvgSalary': 'Avg Salary - Thousands (USD)'})

fig = px.scatter(df, x="Avg Salary - Thousands (USD)", y="Cost of Living Index", text="Country", log_x=True, size_max=100)
fig.update_traces(textposition='top center')
fig.update_layout(title_text='Avg Tech Wage Vs Cost of Living', title_x=0.5)
fig.show()