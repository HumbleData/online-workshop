import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")

print(df["flipper_length_mm"].isnull().sum())