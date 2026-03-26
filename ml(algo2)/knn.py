import math
from collections import Counter

# -----------------------------
# Step 1: Dataset
# -----------------------------
data = [
    [167, 51, "Underweight"],
    [182, 62, "Normal"],
    [176, 69, "Normal"],
    [172, 65, "Normal"],
    [173, 64, "Normal"],
    [174, 56, "Underweight"],
    [169, 58, "Normal"],
    [173, 57, "Normal"],
    [170, 55, "Normal"]
]

# -----------------------------
# Step 2: Test Point & K
# -----------------------------
test_height = 170
test_weight = 57
k = 5

distances = []

# -----------------------------
# Step 3: Calculate Distance Using Loop
# -----------------------------
for row in data:
    height = row[0]
    weight = row[1]
    label = row[2]

    # Euclidean Distance formula
    distance = math.sqrt((test_height - height)**2 +
                         (test_weight - weight)**2)

    distances.append([distance, label])

    print(f"Distance from ({height},{weight}) = {round(distance,2)}")

# -----------------------------
# Step 4: Sort Distances
# -----------------------------
distances.sort()

print("\nSorted Distances:")
for d in distances:
    print(round(d[0],2), d[1])

# -----------------------------
# Step 5: Take K Nearest
# -----------------------------
nearest_neighbors = distances[:k]

labels = []
for neighbor in nearest_neighbors:
    labels.append(neighbor[1])

# -----------------------------
# Step 6: Majority Voting
# -----------------------------
result = Counter(labels).most_common(1)

print("\nFinal Predicted Class:", result[0][0])
