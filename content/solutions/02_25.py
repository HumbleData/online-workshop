import pandas as pd
df = pd.read_csv("../data/Penguins/penguins.csv")
df_2 = df.dropna(how="all")
df_3 = df_2.dropna(how="any")

print(f"number of rows of df_3: {df_3.shape[0]}")