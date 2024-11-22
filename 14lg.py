# Additional Analysis
plt.figure(figsize=(12, 10))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Heart Disease Features')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.close()

X_all = data.drop('target', axis=1)
model_all = LogisticRegression(max_iter=1000)
model_all.fit(X_all, y)

feature_importance = pd.DataFrame({
    'feature': X_all.columns,
    'importance': abs(model_all.coef_[0])
})
feature_importance = feature_importance.sort_values('importance', ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(feature_importance['feature'], feature_importance['importance'])
plt.xlabel('Absolute Coefficient Value')
plt.ylabel('Feature')
plt.title('Feature Importance in Heart Disease Prediction')
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.close()
