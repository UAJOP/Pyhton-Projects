import pandas as pd
import seaborn as sns

pd.set_option("display.max_column", None)

df = sns.load_dataset("car_crashes")

print(df.describe().T)

print(df.info())

print(df.isnull().values.any())

print(df.isnull().sum())

df["alcohol2"] = df["alcohol"] * 2


df["alcohol_new"] = pd.cut(df["alcohol"], [0, 1, 2, 3, 4, 5, 6], labels=["NORMAL","AZ DOZ", "ORTA DOZ", "AŞIRI DOZ", "YÜKSEK DOZ","ABARTI DOZ"])

print(df.head())

df = pd.read_xml("openaq.csv")