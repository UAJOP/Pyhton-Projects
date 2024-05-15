import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")

col_names = ["age", "pclass", "survived", "sex"]
# print(df.loc[((df["age"] > 50) & (df["sex"] == "male")), col_names].head())

print(df.loc[((df["age"] < 30) & (df["sex"] == "female")), col_names].head())



