import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

print(df["sex"].value_counts(dropna=False))