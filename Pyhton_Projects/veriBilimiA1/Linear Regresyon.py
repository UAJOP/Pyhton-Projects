import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("data.csv")

df = df.drop(["Unnamed: 32", "id"], axis=1)

df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})

print(df.info())

X = df.drop("diagnosis",axis=1)
y = df["diagnosis"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=10000, solver="lbfgs")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuary", accuracy)
example_values = {'radius_mean': 6, 'texture_mean': 10, 'perimeter_mean': 60, 'area_mean': 600, 'smoothness_mean': 0.10,
'compactness_mean': 0.02, 'concavity_mean': 0.1, 'concave points_mean': 0.1,
'symmetry_mean': 0.1,
'fractal_dimension_mean': 0.05,
'radius_se': 2,
'texture_se': 0.5,
'perimeter_se': 1,
'area_se': 25,
'smoothness_se': 0.001,
'compactness_se': 0.001,
'concavity_se': 0.1,
'concave points_se': 0.01,
'symmetry_se': 0.02,
'fractal_dimension_se': 0.01,
'radius_worst': 35,
'texture_worst': 25,
'perimeter_worst': 60,
'area_worst': 2000,
'smoothness_worst': 0.1,
'compactness_worst': 0.05,
'concavity_worst': 1,
'concave points_worst': 0.1,
'symmetry_worst': 0.18,
'fractal_dimension_worst': 0.1
}
ornek_degerler = np.array(list(example_values.values())).reshape(1,-1)
tahmin = model.predict(ornek_degerler)
print(tahmin)

