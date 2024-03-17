import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_json("NBA_player_data.json")

#data.columns type = <class 'pandas.core.indexes.base.Index'>
#data type = <class 'pandas.core.frame.DataFrame'>
#individual column type = <class 'pandas.core.series.Series'>

#data.columns = Index(['_id', 'Rk', 'Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA',
    #    'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA',
    #    'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'],
    #   dtype='object')




#Replaces position names with numbers
position_mapping = {"PG": 1, "SG": 2, "SF": 3, "PF": 4, "C": 5}
df["Pos"] = df["Pos"].map(position_mapping)

df = df.dropna(subset=['Pos', 'FT%'])
print(df.dtypes)
y = df["Pos"]
X = df["FT%"]

model = sm.OLS(y,X).fit()
print(model.summary())

plt.scatter(y,X)
plt.show()
