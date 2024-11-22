import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/housing.csv')
df = df.dropna()

x = df['median_income'].values.reshape(-1, 1)
y = df['median_house_value'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

plt.figure(figsize=(10, 6))
plt.scatter(x_test, y_test, color='blue', alpha=0.5)
plt.plot(x_test, y_pred, color='red', linewidth=2)
plt.xlabel('Median Income')
plt.ylabel('House Value')
plt.savefig('house_price.png')
plt.close()