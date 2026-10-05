import json
import pandas as pd


def transform_weather_data(file_path: str, city_name: str) -> pd.DataFrame:

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data["hourly"])
    df["city"] = city_name

    df["time"] = pd.to_datetime(df["time"])

    df["date"] = df["time"].dt.date
    df["hour"] = df["time"].dt.hour
    df["weekday"] = df["time"].dt.day_name()

    return df


if __name__ == "__main__":
    path = "data/raw/rio_de_janeiro_2026-10-01.json"
    df_test = transform_weather_data(path, "rio_de_janeiro")

    print(df_test.head())
    print(df_test.shape)
    print(df_test.isna().sum())
