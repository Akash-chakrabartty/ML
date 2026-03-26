# =====================================================
# SVM HANDWRITTEN DIGIT CLASSIFICATION (MNIST)
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------------------------------
# STEP 1 : Load MNIST Dataset
# -----------------------------------------------------
print("Loading MNIST dataset...")

mnist = fetch_openml('mnist_784', version=1, as_frame=True)

X = mnist.data
y = mnist.target.astype(int)
A
print("Dataset Shape:", X.shape)

# -----------------------------------------------------
# STEP 2 : Normalize Pixel Values
# -----------------------------------------------------
X = X / 255.0

# -----------------------------------------------------
# STEP 3 : Train-Test Split
# -----------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=10000,
    random_state=42
)

# -----------------------------------------------------
# STEP 4 : Train SVM Model
# -----------------------------------------------------
print("Training SVM Model...")

svm_model = SVC(kernel='rbf', gamma='scale')

svm_model.fit(X_train, y_train)

# -----------------------------------------------------
# STEP 5 : Prediction
# -----------------------------------------------------
y_pred = svm_model.predict(X_test)

# -----------------------------------------------------
# STEP 6 : Accuracy
# -----------------------------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy =", round(accuracy*100,2), "%")

# -----------------------------------------------------
# STEP 7 : Confusion Matrix
# -----------------------------------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

# -----------------------------------------------------
# STEP 8 : Classification Report
# -----------------------------------------------------
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -----------------------------------------------------
# STEP 9 : Sample Digit Predictions
# -----------------------------------------------------
plt.figure(figsize=(10,5))

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X_test.iloc[i].values.reshape(28,28), cmap='gray')
    plt.title(f"Predicted: {y_pred[i]}")
    plt.axis('off')

plt.suptitle("Sample Digit Predictions")
plt.show()

# -----------------------------------------------------
# STEP 10 : Accuracy Graph
# -----------------------------------------------------
plt.figure()
plt.bar(["SVM Accuracy"], [accuracy*100])
plt.ylabel("Accuracy (%)")
plt.title("Overall Model Accuracy")
plt.show()