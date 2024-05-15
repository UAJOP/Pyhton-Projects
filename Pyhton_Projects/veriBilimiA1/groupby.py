import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")

print(df["age"].mean())

print(df.groupby("sex").agg({"age": ["mean", "sum", "min", "max"], "survived": "mean"}))

print(df.groupby(["sex", "embark_town"]).agg({"age": ["mean"], "survived": "mean"}))
