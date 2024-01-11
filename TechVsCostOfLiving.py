import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import pandas as pd
import numpy as np


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Country", "Avg Salary", "Cost of Living Index"]

df = pd.read_csv("TechCostOfLiving.csv", usecols=columns)
df.columns = df.columns.str.replace(' ', '')
print("Contents in csv file:", df)
plt.scatter(df.CostofLivingIndex, df.AvgSalary)
plt.show()


#df = pd.read_csv('TechCostOfLiving.csv')

#df.columns = df.columns.str.replace(' ', '') 

#print(df.to_string())  