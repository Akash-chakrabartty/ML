import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Dataset
points = np.array([
    [1.0,1.0],  # A
    [1.2,1.1],  # B
    [0.8,1.2],  # C
    [5.0,5.0],  # D
    [9.0,9.0]   # E
])

labels_name = ['A','B','C','D','E']

# Apply DBSCAN
db = DBSCAN(eps=1.5, min_samples=2)
labels = db.fit_predict(points)

print("Cluster Labels:", labels)

# Plot clusters
plt.scatter(points[:,0], points[:,1], c=labels)

for i, txt in enumerate(labels_name):
    plt.text(points[i,0]+0.05, points[i,1]+0.05, txt)

plt.title("DBSCAN Clustering")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()