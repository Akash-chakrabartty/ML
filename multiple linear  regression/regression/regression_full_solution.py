import numpy as np
import math
import matplotlib.pyplot as plt

# -----------------------------------
# GIVEN DATASET
# -----------------------------------
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([5, 6, 10, 13, 11], dtype=float)

print("X =", X)
print("Y =", Y)

# -----------------------------------
# MEANS
# -----------------------------------
mean_x = np.mean(X)
mean_y = np.mean(Y)

# -----------------------------------
# CALCULATE β1 (SLOPE)
# -----------------------------------
numerator = np.sum((X - mean_x) * (Y - mean_y))
denominator = np.sum((X - mean_x) ** 2)
beta1 = numerator / denominator

# -----------------------------------
# CALCULATE β0 (INTERCEPT)
# -----------------------------------
beta0 = mean_y - beta1 * mean_x

print("\n--- Regression Coefficients ---")
print("β0 (Intercept) =", round(beta0, 3))
print("β1 (Slope)     =", round(beta1, 3))

# -----------------------------------
# PREDICTED VALUES
# -----------------------------------
Y_pred = beta0 + beta1 * X
print("\nPredicted Y =", [round(v, 3) for v in Y_pred])

# -----------------------------------
# RESIDUALS (ERRORS)
# -----------------------------------
residuals = Y - Y_pred
print("Residuals =", [round(v, 3) for v in residuals])

# -----------------------------------
# ERROR METRICS
# -----------------------------------
sse = np.sum(residuals ** 2)
mse = sse / len(X)
rmse = math.sqrt(mse)

# Total Sum of Squares (SST)
sst = np.sum((Y - mean_y) ** 2)

# R-squared
r2 = 1 - (sse / sst)

print("\n--- Error Metrics ---")
print("SSE  =", round(sse, 3))
print("MSE  =", round(mse, 3))
print("RMSE =", round(rmse, 3))
print("SST  =", round(sst, 3))
print("R²   =", round(r2, 3))

# -----------------------------------
# GRAPH: SCATTER PLOT + REGRESSION LINE
# -----------------------------------
plt.figure(figsize=(7, 5))
plt.scatter(X, Y)
plt.plot(X, Y_pred)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression: Best Fit Line")
plt.grid(True)
plt.show()
