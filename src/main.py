from extract import extract_city
from transform import transform_weather_data
from load import load_weather_data


def run_weather_pipeline():
    city = "rio_de_janeiro"
    latitude = -22.9068
    longitude = -43.1729
    target_date = "2026-10-01"

    json_path = extract_city(city, target_date, target_date)
    df = transform_weather_data(json_path, city)
    load_weather_data(df, "data/weather.db")


if __name__ == "__main__":
    run_weather_pipeline()
    print("Pipeline successfully executed!")
