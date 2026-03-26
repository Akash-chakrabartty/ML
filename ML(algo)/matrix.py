# Code Name: CLASSIFICATION_METRICS

# Given confusion matrix values
TP = 22   # Predicted YES & Actual YES
FP = 10   # Predicted YES & Actual NO
FN = 8    # Predicted NO  & Actual YES
TN = 60   # Predicted NO  & Actual NO

total = TP + FP + FN + TN

# Metric calculations
accuracy = (TP + TN) / total
recall = TP / (TP + FN)
precision = TP / (TP + FP)
f1_score = 2 * precision * recall / (precision + recall)

# Output (medium length)
print("True Positive (TP):", TP)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)
print("True Negative (TN):", TN)
print("--------------------------------")
print("Accuracy :", accuracy)
print("Recall   :", recall)
print("Precision:", precision)
print("F1 Score :", f1_score)