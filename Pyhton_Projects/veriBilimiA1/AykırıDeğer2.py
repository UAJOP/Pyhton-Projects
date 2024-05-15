import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("diamonds")
pd.set_option("display.max_column", None)
pd.set_option("display.width", 500)

sns.boxplot(x=df["table"], data=df)
plt.show()


# ALT SINIR BULMAK
q1 = df["table"].quantile(0.25)

q3 = df["table"].quantile(0.75)

IQR = q3-q1

low = q1-1.5*IQR
# EN ALT SINIR

high = q3+1.5*IQR
# ÜST SINIR

print("ALT SINIR", low)

print("ÜST SINIR", high)

print("IQR", IQR)

print("Q1", q1)
print("Q3", q3)

kosul = ((df["table"] < low) | (df["table"] > high))

print(df.loc[kosul, "table"])

#Baskılama Yöntemi
df.loc[(df["table"] > high), "table"] = high
df.loc[(df["table"] < low), "table"] = low


