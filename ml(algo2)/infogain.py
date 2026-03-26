import math
import matplotlib.pyplot as plt

# ----------------------------
# Dataset
# ----------------------------
data = [
    ["YELLOW","SMALL","DIP","ADULT","F"],
    ["YELLOW","LARGE","STRETCH","ADULT","T"],
    ["YELLOW","LARGE","STRETCH","CHILD","F"],
    ["YELLOW","LARGE","DIP","ADULT","F"],
    ["YELLOW","LARGE","DIP","CHILD","F"],
    ["PURPLE","SMALL","STRETCH","ADULT","T"],
    ["PURPLE","SMALL","STRETCH","ADULT","T"],
    ["PURPLE","SMALL","STRETCH","CHILD","F"],
    ["PURPLE","SMALL","DIP","ADULT","F"],
    ["PURPLE","SMALL","DIP","CHILD","F"]
]

attributes = ["Color","Size","Act","Age"]

# ----------------------------
# Entropy Function
# ----------------------------
def entropy(dataset):
    total = len(dataset)
    count_T = sum(1 for row in dataset if row[4] == "T")
    count_F = total - count_T

    if count_T == 0 or count_F == 0:
        return 0

    pT = count_T / total
    pF = count_F / total

    return -(pT * math.log2(pT) + pF * math.log2(pF))

# ----------------------------
# Information Gain Function
# ----------------------------
def information_gain(dataset, column_index):
    total_entropy = entropy(dataset)
    total = len(dataset)

    values = set(row[column_index] for row in dataset)

    weighted_entropy = 0
    for value in values:
        subset = [row for row in dataset if row[column_index] == value]
        weighted_entropy += (len(subset)/total) * entropy(subset)

    return total_entropy - weighted_entropy

# ----------------------------
# Calculate IG for all attributes
# ----------------------------
ig_values = []

print("Information Gain of Each Attribute:\n")

for i in range(4):
    ig = information_gain(data, i)
    ig_values.append(ig)
    print(f"{attributes[i]} : {round(ig,3)}")

# ----------------------------
# Select Best Attribute
# ----------------------------
best_index = ig_values.index(max(ig_values))
print("\nRoot Node Should Be:", attributes[best_index])

# ----------------------------
# Plot Graph
# ----------------------------
plt.figure()
plt.bar(attributes, ig_values)
plt.xlabel("Attributes")
plt.ylabel("Information Gain")
plt.title("Information Gain Comparison")
plt.show()
