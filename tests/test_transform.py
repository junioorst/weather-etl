import os
import json
import pandas as pd
from src.transform import transform_weather_data


def test_transform_weather_data(tmp_path):
    mock_data = {
        "hourly": {
            "time": ["2026-10-01T00:00", "2026-10-01T01:00"],
            "temperature_2m": [20.5, 21.0],
            "relative_humidity_2m": [80, 75],
        }
    }

    d = tmp_path / "raw"
    d.mkdir()
    file_path = d / "mock_weather.json"
    file_path.write_text(json.dumps(mock_data))

    df = transform_weather_data(str(file_path), "porto_alegre")

    assert isinstance(df, pd.DataFrame), "The result must be a Pandas DataFrame"
    assert not df.empty, "The DataFrame cannot be empty"
    assert "city" in df.columns, "The 'city' column should have been added"
    assert (
        df.loc[0, "city"] == "porto_alegre"
    ), "The city name must match the input parameter"
    assert len(df) == 2, "It should contain exactly 2 rows of hourly records"
