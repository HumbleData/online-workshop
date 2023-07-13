import pandas as pd
from IPython.display import display
df = pd.read_csv("../data/Penguins/penguins.csv")

display(df.loc[341:, "bill_length_mm"])