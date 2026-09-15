# 🛰️ Celestia-IoT

Celestia-IoT is a space-themed IoT and data engineering project built around a desktop monitoring terminal.

The project combines ESP32 sensors, external weather and space data, automated data ingestion, PostgreSQL, data transformations and future Data Science experiments.

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

## Current stack
- ESP32
- Python
- PostgreSQL
- SQL
- GitHub Actions
- MkDocs
- dbt
- Pandas / Scikit-learn

## Current status

The initial weather data pipeline is operational:

```text
OpenWeather API
      ↓
Python
      ↓
PostgreSQL
```
Weather data is collected automatically:

- Local machine: 4 times per day
- GitHub Actions: once per day

## Planned

ESP32 sensor integration
ISS and astronomy data
dbt transformations
Data quality checks
Analytics dashboard
ISS observation prediction
Machine Learning experiments
