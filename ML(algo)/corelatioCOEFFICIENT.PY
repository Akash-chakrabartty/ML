# Code Name: PEARSON_CORRELATION_COEFFICIENT

import math
import matplotlib.pyplot as plt

# Given data
demand = [65, 66, 67, 67, 68, 69, 70, 72]
price  = [67, 68, 65, 68, 72, 72, 69, 71]

n = len(demand)

# Mean calculation
mean_demand = sum(demand) / n
mean_price = sum(price) / n

print("Mean Demand =", mean_demand)
print("Mean Price  =", mean_price)
print("--------------------------------")

# Pearson correlation calculation
numerator = 0
den_x = 0
den_y = 0

for i in range(n):
    numerator += (demand[i] - mean_demand) * (price[i] - mean_price)
    den_x += (demand[i] - mean_demand) ** 2
    den_y += (price[i] - mean_price) ** 2

print("Numerator =", numerator)
print("Denominator Part X =", den_x)
print("Denominator Part Y =", den_y)
print("--------------------------------")

correlation = numerator / math.sqrt(den_x * den_y)

print("Correlation Coefficient =", correlation)

# Scatter plot (for extra marks)
plt.scatter(demand, price)
plt.xlabel("Demand")
plt.ylabel("Price")
plt.title("Demand vs Price Correlation")
plt.grid(True)
plt.show()