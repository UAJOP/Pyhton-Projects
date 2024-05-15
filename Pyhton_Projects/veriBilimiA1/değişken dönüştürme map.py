import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import OneHotEncoder
df = sns.load_dataset("tips")
print(df.head())
df["sex"] = df["sex"].map({"Female": 0, "Male": 1})
X = df[["total_bill", "size", "sex"]]
y = df["tip"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(mae)
tahmin_veri = pd.DataFrame({"total_bill": [30], "size": [6], "sex": [1]})
tahmin_tip = model.predict(tahmin_veri)
print(tahmin_tip)
