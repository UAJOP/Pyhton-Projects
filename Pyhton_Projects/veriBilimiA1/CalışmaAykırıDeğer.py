import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("diamonds")

df_table = df["x"]

plt.boxplot(df["x"])
plt.show()

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

t_df = df_table[~aykirilar]
print(t_df.info())

plt.figure(figsize=(8, 6))  # Çizimin boyutunu belirle
plt.boxplot(df["x"],
            patch_artist=True,  # Kutunun rengini doldur
            boxprops=dict(facecolor='lightblue', color='blue'),  # Kutu rengini ve çizgi rengini ayarla
            whiskerprops=dict(color='gray'),  # Whisker (bıyık) çizgilerinin rengini ayarla
            capprops=dict(color='gray'),  # Kutu kenar çizgilerinin rengini ayarla
            medianprops=dict(color='red')  # Medyan çizgisinin rengini ayarla
           )
plt.show()
