import requests
import json
import os

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"
HOURLY_VARS = "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
RAW_DIR = "data/raw"


CITIES = {
    "porto_alegre": {"latitude": -30.03, "longitude": -51.23},
    "rio_de_janeiro": {"latitude": -22.91, "longitude": -43.17},
}


def extract_city(city, start_date, end_date):
    coords = CITIES[city]

    params = {
        "latitude": coords["latitude"],
        "longitude": coords["longitude"],
        "start_date": start_date,
        "end_date": end_date,
        "hourly": HOURLY_VARS,
        "timezone": "America/Sao_Paulo",
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    os.makedirs(RAW_DIR, exist_ok=True)

    path = f"{RAW_DIR}/{city}_{start_date}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"File saved in {path}")
    return path


if __name__ == "__main__":
    for city in CITIES:
        extract_city(city, "2026-10-01", "2026-10-01")
