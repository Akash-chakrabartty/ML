# Code Name: Z_SCORE_NORMALIZATION

import math

print("----- Z SCORE NORMALIZATION -----\n")

# Step 1: Input data
data = [10, 15, 20, 50, 60]
x = 20

print("Input Data:", data)
print("Value to Normalize:", x, "\n")

# Step 2: Calculate Mean
total = 0
for value in data:
    total = total + value
    print("Adding", value, "-> Running Total =", total)

mean = total / len(data)
print("\nMean Calculation Completed")
print("Mean =", mean, "\n")

# Step 3: Calculate Variance
sum_square = 0
for value in data:
    diff = value - mean
    square = diff * diff
    sum_square = sum_square + square
    print("Value:", value, "Difference:", diff, "Square:", square)

variance = sum_square / len(data)
print("\nVariance =", variance)

# Step 4: Standard Deviation
std_dev = math.sqrt(variance)
print("Standard Deviation =", std_dev, "\n")

# Step 5: Z-score Calculation
z_score = (x - mean) / std_dev

print("Z-Score Calculation:")
print("Z =", z_score)

print("\n----- END OF PROGRAM -----")