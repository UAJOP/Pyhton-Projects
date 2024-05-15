import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)


cat_col = [col for col in df.columns if str(df[col].dtypes)
           in ["category", "object", "bool"]]

print(cat_col)

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["float64", "int64"]]

print(num_but_cat)

cat_cols = cat_col + num_but_cat

print(cat_cols)
