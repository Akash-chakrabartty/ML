from sklearn.datasets import load_iris                 
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier   
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd                                   
import numpy as np


data = load_iris()
X = data.data        
y = data.target      
feature_names = data.feature_names
target_names = data.target_names


print("Feature names:", feature_names)
print("Target names (labels):", list(enumerate(target_names)))
print("Total samples:", X.shape[0])
print()


df = pd.DataFrame(X, columns=feature_names)
df['species'] = [target_names[i] for i in y]
print("First 5 rows of the dataset (example):")
print(df.head())
print()


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
print()


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)   
print("Model trained successfully.")
print()


pred = model.predict(X_test)


pred_names = [target_names[i] for i in pred]
true_names = [target_names[i] for i in y_test]


print("Some example predictions (true -> predicted):")
for i in range(len(pred)):
    print(f"{i+1:2d}. {true_names[i]:10s}  ->  {pred_names[i]:10s}")
print()


accuracy = accuracy_score(y_test, pred)
print(f"Accuracy on test set: {accuracy*100:.2f}%")
print()


print("Classification Report:")
print(classification_report(y_test, pred, target_names=target_names))


cm = confusion_matrix(y_test, pred)
cm_df = pd.DataFrame(cm, index=target_names, columns=target_names)
print("Confusion Matrix (rows=true, cols=predicted):")
print(cm_df)
print()


new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])   
new_pred = model.predict(new_sample)
print("Example single prediction for sample [5.1, 3.5, 1.4, 0.2]:")
print("Predicted species:", target_names[new_pred[0]])
print()