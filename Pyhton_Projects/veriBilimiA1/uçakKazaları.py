import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("starbucks.csv")
pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)


print(df.describe().T)

print(df.info())

print(df.isnull().values.any())

print(df.isnull().sum())


cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["float64", "int64"]]

cat_cols = cat_col + num_but_cat

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtypes in ["catagory", "object"]]

num_col = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

num_cols = [col for col in num_col if col not in cat_cols]


print(f"Katogorik değişkenler:{cat_cols}")
print(f"Sayısal değişkenler: {num_cols}")
print(f"Kardinalitesi Yüksekler: {cat_but_car}")

data = df[['Calories', 'Cholesterol (mg)']]

plt.figure(figsize=(10, 6))

sns.scatterplot(x='Calories', y='Cholesterol (mg)', data=data)

plt.title('Calories vs Cholesterol', fontsize=15)

plt.xlabel('Calories', fontsize=12)
plt.ylabel('Cholesterol (mg)', fontsize=12)

plt.show()
