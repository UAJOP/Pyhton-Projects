import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)

cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

print(cat_col)

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["float64", "int64"]]

print(num_but_cat)

cat_cols = cat_col + num_but_cat

# Kardinal değeri yüksek olanlar
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtypes in ["catagory", "object"]]

print(cat_but_car)


# Sayısal değişken Analizi

num_col = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

print(num_col)

num_cols = [col for col in num_col if col not in cat_cols]

print(num_cols)

print(f"Katogorik değişkenler:{cat_cols}")
print(f"Sayısal değişkenler: {num_cols}")
print(f"Kardinalitesi Yüksekler: {cat_but_car}")
