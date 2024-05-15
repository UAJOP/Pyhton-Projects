import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")


# Katagorik Değişken Görselleştirme

print(df["sex"].value_counts())

# CountPlot

sns.countplot(x=df["sex"], data=df)
plt.show()

sns.displot(df["age"], kde=True)
plt.show()

sns.displot(x=df["age"], bins=100, kde=False)
plt.show()

sns.displot(x=df["age"], bins=1000, kde=False)
plt.show()

sns.displot(x=df["age"], bins=10, kde=False)
plt.show()
