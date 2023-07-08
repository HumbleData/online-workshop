import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")
df_2 = df.dropna(how="all")

print(f"number of rows of df_2: {df_2.shape[0]}")