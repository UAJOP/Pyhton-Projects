import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

salaries = [2000, 5000, 4000, 6000]

print(list(map(lambda salary: salary + salary * 20 / 100,salaries)))






pd.set_option("display.max_column",None)
pd.set_option("display.width", 500)

print(df.head())

print(df.info())
print(df.describe().T)




cat_col = [col for col in df.columns if str(df[col].dtypes)in ["category","bool","object"]]
num_col = [col for col in df.columns if str(df[col].dtypes)in ["float64","int64"]]

cat_but_car = [col for col in df.columns if df[col].nunique()>10 and df[col].dtypes in ["category","object","bool"]]

print(f"Sayısal değişkenler : {num_col}")
print(f"Kategorik değişkenler : {cat_col}")
print(f"Kardinal değişkenleri : {cat_but_car}")

for col in num_col:
    print(f"{col}, SINIF DEĞİŞKENİ : {df[col].value_counts()}")


def aykiri_degerler (df,col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3-Q1
    low = Q1-1.5*IQR
    high = Q3+1.5*IQR
    kosul = ((df[col] >= low) | (df[col] <= high))
    temiz_df = df[kosul]
    # clear_df = df[~kosul]
    # ortalama_df = df[kosul] = df.mean()
    # df.loc[(df[col] > high), col] = high
    # df.loc[(df[col] < low), col] = low
    # clear_df = df[kosul]
    return temiz_df

for col in num_col:
    df = aykiri_degerler(df,col)


print(df.describe().T)

for col in num_col:
    if df[col].isnull().any():
        df[col].fillna(df[col].mean(),inplace=True)
        print("boşluk temizlendi")

print(df.isnull().sum())


df["new age"] = pd.cut(df["age"],[1,20,40,60,80,90],labels=["bebek","genç","yetişkin","orta","yaşlı"])


sns.boxplot(x="pclass",y="age",hue="sex", data=df)
plt.show()