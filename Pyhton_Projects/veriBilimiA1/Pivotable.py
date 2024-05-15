import pandas as pd
import seaborn as sns

pd.set_option("display.max_column", None)

df = sns.load_dataset("titanic")


# print(df.pivot_table("survived", "sex", "embarked"))

# print(df.pivot_table("survived", "sex", ["embarked", "class"]))
