import pandas as pd
import seaborn as sns

pd.set_option("display.max_column", None)

df = sns.load_dataset("titanic")

# Yeni değişken oluşturma

df["age2"] = df["age"] * 2

# print(df.head())

df["age_new"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

# print(df.head())

df["age_new2"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90], labels=["Çocuk", "Ergen", "Genç", "Yetişkin", "Yaşlı"])

print(df.head())

new_df = df[["age", "age2"]].apply(lambda x: x/10)

print(new_df.head())
