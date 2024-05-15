import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

print(df.head())
# Pandas Görselleştirme Aracı
df["sex"].value_counts().plot(kind="bar")
plt.show()

# Sayısal Değişken Görselleştirme Aracı

"""
Histogram ya da boxplot yöntemi ile yapılabilir
"""

# Histogram

plt.hist(df["age"])
plt.show()

# Boxplot

plt.boxplot(df["fare"])
plt.show()
