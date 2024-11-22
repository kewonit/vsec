import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/Orange_Telecom_Churn_Data.csv')

plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='total_day_minutes')
plt.title('Histogram of Day Minutes')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(data=df[['total_day_charge', 'total_eve_charge', 'total_night_charge']])
plt.title('Box Plot of Charges')
plt.show()

plt.figure(figsize=(8, 6))
correlation = df[['total_day_minutes', 'total_eve_minutes', 'total_night_minutes']].corr()
sns.heatmap(correlation, annot=True)
plt.title('Correlation Heatmap')
plt.show()