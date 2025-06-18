# fraud_detection_pipeline.py
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Create synthetic data
X, y = make_classification(n_samples=1000, n_features=10, n_informative=6, 
                           n_redundant=2, weights=[0.9, 0.1], random_state=42)

# Prepare DataFrame
df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(10)])
df["is_fraud"] = y

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(df.drop("is_fraud", axis=1), df["is_fraud"], test_size=0.2, random_state=42)

# Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluation
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
