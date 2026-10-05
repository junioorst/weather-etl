import json
import pandas as pd
import sqlite3


def load_weather_data(df: pd.DataFrame, db_path: str) -> None:
    connection = sqlite3.connect(db_path)

    df.to_sql(name="weather_hourly", con=connection, if_exists="replace", index=False)

    connection.close()


if __name__ == "__main__":
    from transform import transform_weather_data

    path_json = "data/raw/rio_de_janeiro_2026-10-01.json"
    df_transf = transform_weather_data(path_json, "rio_de_janeiro")

    database_path = "data/weather.db"

    load_weather_data(df_transf, database_path)

    print("Data loaded successfully into the database!")
