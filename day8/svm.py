# ==========================================================
# Program: SVM on MNIST Dataset
# ==========================================================

# 1- Import Libraries

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import fetch_openml


# 2- Load the MNIST Dataset

mnist = fetch_openml('mnist_784', version=1)

X, y = mnist.data, mnist.target

y = y.astype(int)   # Convert labels to integer


# ⚠ IMPORTANT: Speed er jonno dataset choto kora
# Full 70,000 data nile SVM slow hoye jabe
X = X[:10000]
y = y[:10000]


# 3- Preprocess the Data

# Normalize data to range [0,1]
X = X / 255.0

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 4- Train the SVM Model

# Initialize the SVM classifier
svm_model = SVC(kernel='linear', C=1.0, random_state=42)

# Train the model
svm_model.fit(X_train, y_train)


# 5- Make Predictions

y_pred = svm_model.predict(X_test)


# 6- Evaluate the Model

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n")
print(cm)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# 7- Visualize Results

plt.figure(figsize=(10,8))

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
