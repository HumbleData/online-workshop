import pandas as pd
from IPython.display import display
df = pd.read_csv("../data/Penguins/penguins.csv")

display(df.iloc[-3:, 2])