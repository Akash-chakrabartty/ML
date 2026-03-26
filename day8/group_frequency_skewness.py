# ==========================================================
# Program: Group Frequency Table and Skewness Calculation
# ==========================================================

# Given age groups and frequencies
age_groups = [(2,4), (4,6), (6,8), (8,10)]
frequencies = [16, 13, 7, 5]

# -----------------------------
# Step 1: Create Group Frequency Table
# -----------------------------

print("Age Group\tFrequency\tMidpoint\tfX")

midpoints = []
fx = []
total_f = 0
total_fx = 0

for i in range(len(age_groups)):
    
    lower = age_groups[i][0]
    upper = age_groups[i][1]
    
    midpoint = (lower + upper) / 2     # midpoint calculation
    midpoints.append(midpoint)
    
    f = frequencies[i]
    fx_value = f * midpoint            # f × midpoint
    fx.append(fx_value)
    
    total_f += f
    total_fx += fx_value
    
    print(f"{lower}-{upper}\t\t{f}\t\t{midpoint}\t\t{fx_value}")

print("\nTotal Frequency =", total_f)
print("Sum of fX =", total_fx)


# -----------------------------
# Step 2: Mean Calculation
# -----------------------------

mean = total_fx / total_f
print("\nMean =", round(mean,2))


# -----------------------------
# Step 3: Standard Deviation Calculation
# -----------------------------

sum_f_x2 = 0

for i in range(len(midpoints)):
    deviation = midpoints[i] - mean
    squared = deviation ** 2
    sum_f_x2 += frequencies[i] * squared

variance = sum_f_x2 / total_f
std_dev = variance ** 0.5

print("Standard Deviation =", round(std_dev,2))


# -----------------------------
# Step 4: Mode Calculation (Grouped Data Formula)
# -----------------------------

modal_index = frequencies.index(max(frequencies))

L = age_groups[modal_index][0]
fm = frequencies[modal_index]
fm1 = frequencies[modal_index - 1] if modal_index > 0 else 0
fm2 = frequencies[modal_index + 1] if modal_index < len(frequencies)-1 else 0
h = age_groups[modal_index][1] - age_groups[modal_index][0]

mode = L + ((fm - fm1) / ((fm - fm1) + (fm - fm2))) * h

print("Mode =", round(mode,2))


# -----------------------------
# Step 5: Karl Pearson Skewness
# -----------------------------

# Skewness = (Mean - Mode) / Standard Deviation

skewness = (mean - mode) / std_dev

print("Skewness =", round(skewness,3))
