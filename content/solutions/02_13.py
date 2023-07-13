import pandas as pd
from IPython.display import display
df = pd.read_csv("../data/Penguins/penguins.csv")

display(df.iloc[[145, 7, 0], [4, -2]])