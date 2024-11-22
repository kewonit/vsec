# Optional: Feature importances
print("\nFeature Importances:")
for feature, importance in zip(x.columns, dt_classifier.feature_importances_):
    print(f"{feature}: {importance}")

plt.figure(figsize=(10,6))
importances = pd.Series(dt_classifier.feature_importances_, index=x.columns).sort_values(ascending=True)
importances.plot(kind='barh')
plt.title('Feature Importance in Decision Tree')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=300)