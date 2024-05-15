# loc -> string based selection

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")

print(df.loc[0:3, "age"])
# 3. sütunuda dahil eder

col_names = ["age", "alive", "embarked"]
print(df.loc[0:5, col_names])

print(df.loc[0:3, "survived":"age"])

