import pandas as pd
from IPython.display import display
df = pd.read_csv("../data/Penguins/penguins.csv")

display(df.loc[[145, 7, 0], ["flipper_length_mm", "body_mass_g"]])