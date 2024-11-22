import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv('datasets/heart.csv')

# Original Logistic Regression Plot
X = data['oldpeak'].values.reshape(-1, 1)
y = data['target']
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

X_test = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
y_pred = model.predict_proba(X_test)[:, 1]

plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='black', s=20, alpha=0.5, label='Data points')
plt.plot(X_test, y_pred, 'r-', label='Logistic Regression', linewidth=2)
plt.xlabel('ST Depression (oldpeak)')
plt.ylabel('Probability of Heart Disease')
plt.title('Logistic Regression: ST Depression vs Heart Disease')
plt.grid(True)
plt.legend()
plt.savefig('logistic_curve.png')
plt.close()