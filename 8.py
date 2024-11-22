import pandas as pd

df = pd.read_csv('datasets/Heart.csv')

print("Original Dataset")
print(df)
print("\n")

df_drop = df.dropna()
print("After dropping missing values")
print(df_drop)
print("\n")

df_fill = df.fillna(0)
print("After filling with zero")
print(df_fill)
print("\n")

df_mean = df.fillna(df.mean())
print("After filling with mean")
print(df_mean)