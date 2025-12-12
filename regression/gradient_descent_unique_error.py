import numpy as np

# --------------------------
# GIVEN DATA
# --------------------------
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([5, 6, 10, 13, 11], dtype=float)

# --------------------------
# INITIAL WRONG VALUES (Sir's example)
# --------------------------
beta0 = 3.0
beta1 = 1.9

learning_rate = 1   # Sir used ×1 in board

print("\n---------------------------")
print(" UNIQUE ERROR: 10 ITERATIONS")
print("---------------------------\n")

for itr in range(1, 11):  # 10 iterations
    # Predictions with current beta0, beta1
    Y_pred = beta0 + beta1 * X

    # Errors (Ŷ - Y)
    errors = Y_pred - Y

    # Summations
    sum_error = np.sum(errors)
    sum_error_x = np.sum(errors * X)

    # Update rules (Sir's formula)
    beta0 = beta0 - learning_rate * sum_error
    beta1 = beta1 - learning_rate * sum_error_x

    print(f"Iteration {itr}:")
    print(f"  Sum Error      = {sum_error:.4f}")
    print(f"  Sum Error * X  = {sum_error_x:.4f}")
    print(f"  Updated β0     = {beta0:.4f}")
    print(f"  Updated β1     = {beta1:.4f}")
    print("---------------------------")

print("\nFinal Estimated Values after 10 iterations:")
print(f"β0 = {beta0:.4f}")
print(f"β1 = {beta1:.4f}")
