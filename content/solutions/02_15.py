import pandas as pd
from IPython.display import display
df = pd.read_csv("../data/Penguins/penguins.csv")

mask_PW_PL = (df["body_mass_g"] > 4000) & (df["flipper_length_mm"] < 185)
display(df[mask_PW_PL])