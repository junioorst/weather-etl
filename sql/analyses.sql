-- 1. General Overview: Overall average temperature and humidity per city
SELECT 
    city,
    ROUND(AVG(temperature_2m), 2) AS avg_temperature,
    ROUND(AVG(relative_humidity_2m), 2) AS avg_humidity
FROM weather_hourly
GROUP BY city;

-- 2. Extremes: Hottest and coldest recorded hours per city
SELECT 
    city,
    MAX(temperature_2m) AS max_temperature,
    MIN(temperature_2m) AS min_temperature
FROM weather_hourly
GROUP BY city;

-- 3. Daily Aggregations: Daily trends (max, min, and average temperature per day)
-- Extracts the date part from the timestamp string for grouping
SELECT 
    city,
    SUBSTR(time, 1, 10) AS observation_date,
    ROUND(MAX(temperature_2m), 2) AS daily_max_temp,
    ROUND(MIN(temperature_2m), 2) AS daily_min_temp,
    ROUND(AVG(temperature_2m), 2) AS daily_avg_temp
FROM weather_hourly
GROUP BY city, observation_date
ORDER BY observation_date DESC;