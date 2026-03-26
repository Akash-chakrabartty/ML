# ==========================================================
# Program: Calculate Mean, Median, Mode for Grouped Data
# ==========================================================

# Given Class Intervals and Frequencies

classes = [(0,9), (10,19), (20,29), (30,39), (40,49),
           (50,59), (60,69), (70,79), (80,89)]

frequency = [20, 21, 23, 16, 11, 10, 7, 3, 1]


# ----------------------------------------------------------
# 1️⃣ Estimated Mean
# ----------------------------------------------------------

# Step 1: Midpoint calculate করা
midpoints = []

for c in classes:
    midpoint = (c[0] + c[1]) / 2
    midpoints.append(midpoint)

# Step 2: f × midpoint calculate করা
fx = []

for i in range(len(frequency)):
    fx_value = frequency[i] * midpoints[i]
    fx.append(fx_value)

# Step 3: Sum বের করা
total_f = sum(frequency)
total_fx = sum(fx)

# Step 4: Mean formula
mean = total_fx / total_f

print("Total Frequency (n):", total_f)
print("Sum of fX:", total_fx)
print("Estimated Mean =", round(mean,2))


# ----------------------------------------------------------
# 2️⃣ Estimated Median
# ----------------------------------------------------------

# Step 1: n/2 বের করা
n = total_f
n_half = n / 2

# Step 2: Cumulative Frequency বের করা
cumulative = []
cum_sum = 0

for f in frequency:
    cum_sum += f
    cumulative.append(cum_sum)

# Step 3: Median class বের করা
for i in range(len(cumulative)):
    if cumulative[i] >= n_half:
        median_index = i
        break

# Formula variables
L = classes[median_index][0] - 0.5   # lower boundary
B = cumulative[median_index - 1]     # cumulative before median class
G = frequency[median_index]          # freq of median class
W = classes[median_index][1] - classes[median_index][0] + 1  # class width

# Median formula
median = L + ((n_half - B) / G) * W

print("\nEstimated Median =", round(median,2))


# ----------------------------------------------------------
# 3️⃣ Estimated Mode
# ----------------------------------------------------------

# Step 1: Modal class index (highest frequency)
modal_index = frequency.index(max(frequency))

L_mode = classes[modal_index][0] - 0.5
fm = frequency[modal_index]
fm1 = frequency[modal_index - 1]
fm2 = frequency[modal_index + 1]
W_mode = classes[modal_index][1] - classes[modal_index][0] + 1

# Mode formula
mode = L_mode + ((fm - fm1) / ((fm - fm1) + (fm - fm2))) * W_mode

print("Estimated Mode =", round(mode,2))
