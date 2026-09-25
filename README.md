# 🛰️ Celestia-IoT

Applied Meteorology | Scientific Python & Weather Data Engineering

Celestia-IoT is an end-to-end environmental and space-data platform combining automated weather API ingestion, PostgreSQL/Supabase storage, SQL transformations, scientific Python analysis, and ESP32-based local sensing.

The project explores meteorological observations, derived atmospheric variables, data quality, and the comparison of external weather data with local sensor measurements.

## Architecture

```text
ESP32 + Sensors ──┐
                  ├──> Python Ingestion ──> PostgreSQL
Weather APIs ─────┘                            │
                                              ▼
                                             dbt
                                              │
                                    ┌─────────┴─────────┐
                                    ▼                   ▼
                                Analytics              ML
```

Weather data is collected automatically:

- GitHub Actions: 4 times per day


## Planned stack

DATA ENGINEERING
API → GitHub Actions → PostgreSQL/Supabase → dbt :heavy_check_mark:

SCIENTIFIC PYTHON
Pandas → NumPy → meteorological calculations

DATA SCIENCE
feature engineering → correlations → time series → ML

IOT
ESP32 → AHT20/BMP280 → telemetry → database


```
