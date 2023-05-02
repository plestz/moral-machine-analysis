import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math as math

pd.options.display.max_rows = 100

# import data
df = pd.read_csv('/Users/paul/Desktop/CSCI1952B/av-final/analysis/data/SharedResponses.csv', nrows=10000)

# print(df.head(10))

# print(df.describe())

# print(df.info())

# clean data: remove rows with empty cells
new_df = df.dropna()

# print(new_df.describe())

print(new_df.columns)

des_df = new_df[['NumberOfCharacters', 'Intervention']]

# print(des_df.head(10))

# print(new_df.info())

sns.scatterplot(x='NumberOfCharacters',y='Intervention', data=des_df)

plt.show()