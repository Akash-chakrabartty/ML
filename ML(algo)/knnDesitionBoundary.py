# Code Name: KNN_DECISION_BOUNDARY_ADVANCED_VISUAL (VERTICAL)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# -----------------------------
# Step 1: Dataset
# -----------------------------

# Class 0 (Circles)
X_circle = np.array([
    [1,2], [1.5,2.5], [2,1.5], [2,2.8],
    [2.5,2], [3,1.2], [3.2,1.8], [3.5,2.5]
])

# Class 1 (Diamonds)
X_diamond = np.array([
    [4.5,3.5], [5,4], [5.2,3.8],
    [4.8,4.2], [5,3.2]
])

X = np.vstack((X_circle, X_diamond))
y = np.array([0]*len(X_circle) + [1]*len(X_diamond))

# -----------------------------
# Step 2: Create mesh grid
# -----------------------------
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 400),
    np.linspace(y_min, y_max, 400)
)

grid = np.c_[xx.ravel(), yy.ravel()]

# -----------------------------
# Step 3: Multiple K values
# -----------------------------
k_values = [1, 3, 5]

plt.figure(figsize=(7, 15))   # 🔑 Tall figure for vertical layout

for idx, k in enumerate(k_values, 1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)

    Z = knn.predict(grid)
    Z = Z.reshape(xx.shape)

    # 🔑 KEY CHANGE: 3 rows, 1 column
    plt.subplot(3, 1, idx)

    plt.contourf(xx, yy, Z, alpha=0.35, cmap=plt.cm.coolwarm)

    plt.scatter(X_circle[:,0], X_circle[:,1],
                c='dodgerblue', edgecolor='black',
                marker='o', s=120, label='Class 0')

    plt.scatter(X_diamond[:,0], X_diamond[:,1],
                c='crimson', edgecolor='black',
                marker='D', s=120, label='Class 1')

    plt.title(f"KNN Decision Boundary (k = {k})")
    plt.xlabel("x2")
    plt.ylabel("x1")
    plt.grid(True)

    if idx == 1:
        plt.legend()

plt.suptitle(
    "Nearest Neighbour Decision Boundaries (Different k values)",
    fontsize=14,
    fontweight='bold'
)

plt.tight_layout()
plt.show()