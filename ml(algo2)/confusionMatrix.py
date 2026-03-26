import matplotlib.pyplot as plt

# Given confusion matrix values
TP = 150
FP = 10
FN = 20
TN = 120

# Calculate TPR and FPR
TPR = TP / (TP + FN)   # Sensitivity
FPR = FP / (FP + TN)   # False Positive Rate

print("TPR:", round(TPR,3))
print("FPR:", round(FPR,3))

# ROC curve points
x = [0, FPR, 1]
y = [0, TPR, 1]

# Plot ROC Curve
plt.figure()
plt.plot(x, y)
plt.plot([0,1], [0,1])  # Diagonal reference line

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()
