# Weather ETL Pipeline 🌦️

A modular and lightweight ETL (Extract, Transform, Load) pipeline built in Python to fetch meteorological data from an open API, process and transform it using Pandas, store it securely in a local SQLite database, validate logic with automated tests, and extract insights using SQL.

---

## 🚀 Project Structure

```text
weather-etl/
│
├── data/
│   ├── raw/              # Raw JSON responses fetched from the API
│   └── weather.db        # SQLite database storing processed weather records
│
├── sql/
│   └── analyses.sql      # Analytical SQL queries for data insights
│
├── src/
│   ├── extract.py        # Extracts raw weather data from API
│   ├── transform.py      # Cleans, structures, and transforms data
│   ├── load.py           # Loads processed data into SQLite
│   └── main.py           # Orchestrates the full ETL pipeline
│
├── tests/
│   └── test_transform.py # Unit tests for transformation logic
│
├── .gitignore
├── pytest.ini            # Pytest configuration
├── README.md
└── requirements.txt      # Project dependencies
```

---

## 🛠️ Technologies Used
* **Python 3.12+**
* **Pandas** (Data manipulation and transformation)
* **Pytest** (Automated unit testing)
* **SQLite** (Local database storage and SQL analytics)
* **VS Code & SQLite Extensions**

---

## ⚙️ How to Run

1. **Clone the repository and enter the project folder:**
   ```bash
   git clone <repository-url>
   cd weather-etl
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the ETL pipeline:**
   ```bash
   python src/main.py
   ```

---

## 🧪 Running Tests

This project uses `pytest` for automated testing. To run the unit tests, execute:
```bash
pytest
```

---

## 📊 SQL Analytics

You can run the analytical queries located in `sql/analyses.sql` directly against your `data/weather.db` database using an SQLite viewer or CLI to inspect overall averages, extreme temperatures, and daily trends.