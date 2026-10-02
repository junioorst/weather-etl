import requests
import json
import os

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude":-30.03,
    "longitude":-51.23,
    "start_date":"2026-10-01",
    "end_date":"2026-10-01",
    "hourly":"temperature_2m,precipitation,wind_speed_10m",
    "timezone":"America/Sao_Paulo",
}

response = requests.get(url, params=params, timeout=30)

data = response.json()
os.makedirs("data/raw", exist_ok=True)

path = f"data/raw/porto_alegre_{params['start_date'].json}"

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"File saved in {path}")