# =====================================================
# Program: Standard Error Calculation Using Array & Loop
# =====================================================

# Given data array (multiple values dhore general format e likhlam)
sample_sizes = [200]          # sample size list
standard_deviations = [180]   # standard deviation list
means = [550]                 # mean list (given but SE te use hoy na)

# Loop diye calculation
for i in range(len(sample_sizes)):
    
    n = sample_sizes[i]
    sd = standard_deviations[i]
    mean = means[i]
    
    # Step 1: square root manually calculate using power
    sqrt_n = n ** 0.5      # √n
    
    # Step 2: Standard Error formula apply
    # SE = SD / √n
    standard_error = sd / sqrt_n
    
    # Output
    print("Sample Size (n):", n)
    print("Mean Score:", mean)
    print("Standard Deviation:", sd)
    print("Square Root of n:", round(sqrt_n, 4))
    print("Standard Error =", round(standard_error, 2))
