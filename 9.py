import pandas as pd
import numpy as np

df = pd.read_csv('datasets/iris.csv')

numeric_cols = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']

for col in numeric_cols:
    z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
    df = df[z_scores < 3]

print(df)