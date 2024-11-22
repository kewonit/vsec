import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/iris.csv')
df = df.drop('species', axis=1)

corr = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True)
plt.show()