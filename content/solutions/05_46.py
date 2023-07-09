import pandas as pd
import datetime

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

dict_capitals = {
    "Denmark": "copenhague",
    "France": "paris",
    "Italy": "rome",
    "Spain": "madrid",
    "United Kingdom": "london",
}

unknown_city = df["city"] == "unknown"
df.loc[unknown_city, "city"] = df.loc[unknown_city, "country"].map(dict_capitals)

dict_cities = df.loc[df['country'].notnull(), ['city', 'country']].set_index('city').to_dict()['country']

dict_cities.update(
    {
        "bristol": "United Kingdom",
        "gothenburg": "Sweden",
        "graz": "Austria",
        "lyon": "France",
        "murcia": "Spain",
        "parma": "Italy",
    },
)

null_country = df["country"].isnull()
df.loc[null_country, "country"] = df.loc[null_country, "city"].map(dict_cities)

df["country"].value_counts(dropna=False)


def f(x):
    if x == 1:
        return "single"
    else:
        return "multiple"

df["Attendees"].apply(f)

languages = pd.read_csv("../data/food_training/languages.csv")

df = df.merge(languages, how="left", left_on="country", right_on="Country")

df = df.drop("Country", axis=1)

df["DateFrom"] = pd.to_datetime(df["DateFrom"], format="%Y-%m-%d")
df["DateTo"] = pd.to_datetime(df["DateTo"], format="%Y-%m-%d")

df["duration"] = df["DateTo"] - df["DateFrom"] + datetime.timedelta(days=1)

df["month"] = df["DateFrom"].dt.month
df.sort_values(["duration", "Attendees"], ascending=[True, False])

print('df_gr = df.groupby("city")')
df_gr = df.groupby("city")

