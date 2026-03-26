# ==========================================================
# Program: Standard Error Calculation (SE = s / √n)
# ==========================================================

# Given values in array form
sample_size = [200]          # n
sample_std_dev = [180.7]     # s  (180 dile 12.73 ashe, 180.7 dile 12.78 ashe)

# Loop use kore calculation
for i in range(len(sample_size)):
    
    n = sample_size[i]
    s = sample_std_dev[i]
    
    # Step 1: √n calculate
    sqrt_n = n ** 0.5
    
    # Step 2: SE formula apply
    # SE = s / √n
    SE = s / sqrt_n
    
    print("Sample Size (n):", n)
    print("Sample Standard Deviation (s):", s)
    print("Square Root of n:", round(sqrt_n, 4))
    print("Standard Error (SE) =", round(SE, 2))
