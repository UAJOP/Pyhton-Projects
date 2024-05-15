# Saçılım Grafiği
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)

print(df.head())

sns.scatterplot(x="total_bill", y="tip", hue="day", size="size", data=df)

plt.show()



