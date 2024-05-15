# iloc -> intager based selection

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
print(df.head())

print(df.iloc[0:3, 0:2])
