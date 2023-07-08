import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

print(df["species"].value_counts(normalize=True))