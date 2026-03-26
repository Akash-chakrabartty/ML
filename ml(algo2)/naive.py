import math
import matplotlib.pyplot as plt

A = [3,4,1]
B = [7,1,5]

# Differences
diff = [abs(a-b) for a,b in zip(A,B)]

# Euclidean
euclidean = math.sqrt(sum((a-b)**2 for a,b in zip(A,B)))

# Manhattan
manhattan = sum(diff)

# Minkowski (p=3)
p = 3
minkowski = (sum(abs(a-b)**p for a,b in zip(A,B)))**(1/p)

# Cosine Distance
dot = sum(a*b for a,b in zip(A,B))
magA = math.sqrt(sum(a*a for a in A))
magB = math.sqrt(sum(b*b for b in B))
cosine_similarity = dot / (magA * magB)
cosine_distance = 1 - cosine_similarity

print("Euclidean Distance:", round(euclidean,3))
print("Manhattan Distance:", manhattan)
print("Minkowski Distance (p=3):", round(minkowski,3))
print("Cosine Distance:", round(cosine_distance,3))

# Graph
names = ["Euclidean","Manhattan","Minkowski(p=3)","Cosine"]
values = [euclidean, manhattan, minkowski, cosine_distance]

plt.figure()
plt.bar(names, values)
plt.xlabel("Distance Type")
plt.ylabel("Value")
plt.title("Distance Comparison")
plt.show()
