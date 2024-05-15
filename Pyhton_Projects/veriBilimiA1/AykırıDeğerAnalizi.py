import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("diamonds")


df_table = df["table"]

q1 = df_table.quantile(0.25)
q2 = df_table.quantile(0.50)
q3 = df_table.quantile(0.75)

IQR = q3 - q1
print("Q1", q1)
print("Q3", q3)
print("IQR", IQR)

low_level = q1 - 1.5 * IQR
high_level = q3 + 1.5 * IQR

print("ALT SINIR :", low_level)
print("ÜST SINIR :", high_level)

aykirilar = ((df_table < low_level) | (df_table > high_level))

print("Aykırılar", aykirilar)
print(df_table[aykirilar])

print(df_table[aykirilar].index)

# silme
t_df = df_table[~aykirilar]
print(t_df.info())

# ortalama
df_table = pd.DataFrame(df_table)
# data frame formatına dönüştürme
df_table[aykirilar] = df_table.mean()
print(t_df.info())




