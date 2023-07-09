import pandas as pd

df_2014 = pd.read_csv("../data/food_training/training_2014.csv", header=1)
df_2015 = pd.read_csv("../data/food_training/training_2015.csv", header=1)
df_2016 = pd.read_csv("../data/food_training/training_2016.csv", header=1)

frames = [df_2014, df_2015, df_2016]
df = pd.concat(frames)

df = df.reset_index()
df.index

cols_to_remove = ["Unnamed: 5", "Unnamed: 6"]
df = df.drop(cols_to_remove, axis=1)

df[["city", "country"]] = df["Location"].str.split(pat=";", expand=True)

df = df.drop("Location", axis=1)

df["city"] = df["city"].str.lower()

df["city"] = df["city"].str.replace(r"/\w*", "", regex=True)

dict_codes = {
    "BG": "Bulgaria",
    "CZ": "Czech Republic",
    "IT": "Italy",
    "GR": "Greece",
    "SI": "Slovenia",
    "UK": "United Kingdom",
}

country_in_codes = df["country"].isin(dict_codes.keys())
df.loc[country_in_codes, "country"] = df.loc[country_in_codes, "country"].map(dict_codes)

print('df.loc[country_in_codes, "country"] = df.loc[country_in_codes, "country"].map(dict_codes)')