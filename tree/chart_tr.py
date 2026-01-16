import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Dataset
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

# Encode target
le = LabelEncoder()
df['Decision'] = le.fit_transform(df['Decision'])

X = df[['Income', 'LawnSize']]
y = df['Decision']

# -----------------------------
# CART Model
# -----------------------------
model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=3,
    min_samples_leaf=2
)
model.fit(X, y)

# -----------------------------
# BEAUTIFUL TREE PLOT
# -----------------------------
plt.figure(figsize=(20, 10))  # BIG size

plot_tree(
    model,
    feature_names=['Income', 'Lawn Size'],
    class_names=['Nonowner', 'Owner'],
    filled=True,              # COLOR FILLED
    rounded=True,             # ROUND BOX
    fontsize=12               # READABLE TEXT
)

plt.title("CART Decision Tree using Gini Index", fontsize=16)
plt.show()
