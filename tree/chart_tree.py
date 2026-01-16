import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Step 1: Create Dataset
# -----------------------------
data = {
    'Income': [60,75,85.5,52.8,64.8,64.8,51.5,43.2,87,84,
               110.1,49.2,108,52.2,92.8,66,69,47.4,93,33,
               51,51,81,63],

    'LawnSize': [18.4,19.6,16.8,20.8,21.6,17.2,20.8,20.4,23.6,17.6,
                 19.2,17.6,17.6,16,22.4,18.4,20,16.4,20.8,18.8,
                 22,14,20,14],

    'Decision': ['Owner','Nonowner','Owner','Nonowner','Owner','Nonowner',
                 'Owner','Nonowner','Owner','Nonowner','Owner','Nonowner',
                 'Owner','Nonowner','Owner','Nonowner','Owner','Nonowner',
                 'Owner','Nonowner','Owner','Nonowner','Owner','Nonowner']
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Scatter Plot
# -----------------------------
owner = df[df['Decision'] == 'Owner']
nonowner = df[df['Decision'] == 'Nonowner']

plt.figure(figsize=(8,6))
plt.scatter(owner['Income'], owner['LawnSize'], label='Owner')
plt.scatter(nonowner['Income'], nonowner['LawnSize'], label='Nonowner')
plt.xlabel("Income")
plt.ylabel("Lawn Size")
plt.title("Income vs Lawn Size Distribution")
plt.legend()
plt.show()

# -----------------------------
# Step 3: Encode Target
# -----------------------------
le = LabelEncoder()
df['Decision'] = le.fit_transform(df['Decision'])
# Owner = 1, Nonowner = 0

X = df[['Income', 'LawnSize']]
y = df['Decision']

# -----------------------------
# Step 4: CART Decision Tree
# -----------------------------
model = DecisionTreeClassifier(criterion='gini', max_depth=3)
model.fit(X, y)

# -----------------------------
# Step 5: Plot Decision Tree
# -----------------------------
plt.figure(figsize=(14,8))
plot_tree(
    model,
    feature_names=['Income', 'LawnSize'],
    class_names=['Nonowner', 'Owner'],
    filled=True
)
plt.title("CART Decision Tree using Gini Index")
plt.show()
