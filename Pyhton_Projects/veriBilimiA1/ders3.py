# Seaborn
import seaborn as sns

df = sns.load_dataset("titanic")

print(df.info())
# BU VERİ TİPİ HAKKINDA BİLGİ SAĞLAR

print(df.describe().T)
# BU VERİ TİPİNDE Kİ MATEMATİKSEL İFADELİRİ ANALİZ EDE

print(df.isnull().values.any())
# Boşluk analizi

print(df.isnull().sum())
# Değişkenlerde kaç boşluk var

print(df.head())
print(df["sex"].head())

print(df["sex"].value_counts())

print(df["embarked"].value_counts())


