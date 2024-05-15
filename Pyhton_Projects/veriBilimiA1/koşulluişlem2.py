import pandas as pd
import seaborn as sns

# pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")

kosul = ((df["age"] > 50) & (df["sex"] == "male") & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")))
getir = ["age", "class", "embark_town"]
df_new = df.loc[kosul, getir]
print(df_new.head())
