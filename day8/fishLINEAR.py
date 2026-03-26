# ==========================================================
# Program: Simple Linear Regression (Weight vs Length)
# ==========================================================

# -----------------------------
# Data for Bream
# -----------------------------

bream_length = [25.4, 26.3, 26.5, 29, 29.7, 37]
bream_weight = [242, 290, 340, 363, 500, 1000]

# -----------------------------
# Data for Roach
# -----------------------------

roach_length = [23.5, 25.2, 26, 31.7, 22.5, 20.8, 14.5]
roach_weight = [200, 180, 290, 390, 160, 140, 40]


# ==========================================================
# Function to Calculate Regression Coefficients
# ==========================================================

def linear_regression(x, y, species_name):
    
    n = len(x)
    
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    
    # Step 1: Summations calculate
    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_xy += x[i] * y[i]
        sum_x2 += x[i] ** 2
    
    # Step 2: Calculate slope (b1)
    # Formula:
    # b1 = (nΣxy - ΣxΣy) / (nΣx² - (Σx)²)
    
    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = (n * sum_x2) - (sum_x ** 2)
    
    b1 = numerator / denominator
    
    # Step 3: Calculate intercept (b0)
    # b0 = (Σy - b1Σx) / n
    
    b0 = (sum_y - (b1 * sum_x)) / n
    
    # Output
    print("\nSpecies:", species_name)
    print("Slope (b1) =", round(b1, 4))
    print("Intercept (b0) =", round(b0, 4))
    print("Regression Equation:")
    print("Weight =", round(b0,4), "+", round(b1,4), "* Length")


# ==========================================================
# Run for Both Species
# ==========================================================

linear_regression(bream_length, bream_weight, "Bream")
linear_regression(roach_length, roach_weight, "Roach")
