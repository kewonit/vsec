import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/iris.csv')

plt.figure(figsize=(8, 6))
plt.scatter(df['sepal.length'], df['sepal.width'])
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.title('Sepal Length vs Width')
plt.show()

print(df.describe())

plt.figure(figsize=(8, 6))
df.boxplot()
plt.title('Box Plot')
plt.show()