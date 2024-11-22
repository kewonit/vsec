import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/Admission_Predict.csv')
df['Admitted'] = (df['Chance of Admit '] >= 0.75).astype(int)

x = df[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']]
y = df['Admitted']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

dt_classifier = DecisionTreeClassifier(random_state=42, max_depth=3) 
dt_classifier.fit(x_train_scaled, y_train)

y_pred = dt_classifier.predict(x_test_scaled)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(25,12))
plot_tree(dt_classifier, 
          feature_names=x.columns,
          class_names=['Not Admitted', 'Admitted'],
          filled=True,
          rounded=True,
          proportion=True,
          impurity=True,
          precision=2)
plt.title('Admission Decision Tree', pad=20, size=16)
plt.savefig('decision_tree.png', dpi=300)