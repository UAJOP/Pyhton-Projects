import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("diamonds")
pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)

print(df.head())

print(df.isnull().sum())

df_son = df.dropna()
print(df_son.isnull().sum())


df["age"].fillna(0)

df["age"].fillna(df["age"].mean())

