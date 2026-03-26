import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Dataset
points = np.array([
    [2,3],   # A
    [3,4],   # B
    [5,8],   # C
    [6,9],   # D
    [8,10]   # E
])

labels = ['A','B','C','D','E']

# Perform hierarchical clustering
Z = linkage(points, method='average', metric='euclidean')

print("Linkage Matrix:\n", Z)

# Plot dendrogram
plt.figure()
dendrogram(Z, labels=labels)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Points")
plt.ylabel("Distance")

plt.show()