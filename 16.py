import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('datasets/Admission_Predict.csv')
df['Admitted'] = (df['Chance of Admit '] >= 0.75).astype(int)

x = df[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']]
y = df['Admitted']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(x_train_scaled, y_train)

y_pred = dt_classifier.predict(x_test_scaled)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Optional: Feature importances
print("\nFeature Importances:")
for feature, importance in zip(x.columns, dt_classifier.feature_importances_):
    print(f"{feature}: {importance}")