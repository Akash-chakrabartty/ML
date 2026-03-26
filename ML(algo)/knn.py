# Code Name: KNN_ANIMAL_PREDICTION_VISUAL

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# ---------------------------------
# Step 1: Dataset
# ---------------------------------

# Features: [Weight, Height]
X = np.array([
    [4,35],   # Cat
    [6,40],   # Dog
    [3,25],   # Cat
    [7,45],   # Dog
    [5,30],   # Cat
    [8,50],   # Dog
    [2,20],   # Cat
    [5,35]    # Dog
])

# Labels: Cat = 0, Dog = 1
y = np.array([0,1,0,1,0,1,0,1])

# New animal
new_animal = np.array([[4,30]])

# ---------------------------------
# Step 2: Train KNN (k = 5)
# ---------------------------------
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X, y)

prediction = knn.predict(new_animal)

# ---------------------------------
# Step 3: Print prediction
# ---------------------------------
species = "Cat" if prediction[0] == 0 else "Dog"
print("Predicted Species of New Animal:", species)

# ---------------------------------
# Step 4: Graph 1 - Dataset with new point
# ---------------------------------
plt.figure(figsize=(7,6))

cats = X[y == 0]
dogs = X[y == 1]

plt.scatter(cats[:,0], cats[:,1],
            c='orange', marker='o', s=120, label='Cat')

plt.scatter(dogs[:,0], dogs[:,1],
            c='green', marker='^', s=120, label='Dog')

plt.scatter(new_animal[:,0], new_animal[:,1],
            c='red', marker='*', s=250, label='New Animal')

plt.xlabel("Weight (Kg)")
plt.ylabel("Height (Cm)")
plt.title("Animal Dataset with New Animal")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------
# Step 5: Graph 2 - Decision Boundary
# ---------------------------------
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-5, X[:,1].max()+5

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 300),
    np.linspace(y_min, y_max, 300)
)

grid = np.c_[xx.ravel(), yy.ravel()]
Z = knn.predict(grid)
Z = Z.reshape(xx.shape)

plt.figure(figsize=(7,6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Pastel1)

plt.scatter(cats[:,0], cats[:,1],
            c='orange', marker='o', s=120, label='Cat')

plt.scatter(dogs[:,0], dogs[:,1],
            c='green', marker='^', s=120, label='Dog')

plt.scatter(new_animal[:,0], new_animal[:,1],
            c='red', marker='*', s=250, label='New Animal')

plt.xlabel("Weight (Kg)")
plt.ylabel("Height (Cm)")
plt.title("KNN Decision Boundary (k = 5)")
plt.legend()
plt.grid(True)
plt.show()