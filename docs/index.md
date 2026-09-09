# Celestia-IoT

> A small open-source space and environmental data station.

Celestia-IoT is a desktop device based on ESP32 that combines:

- environmental sensors
- space data
- ISS pass information
- OLED interface
- Wi-Fi connectivity
- data engineering pipelines
- analytics and machine learning

## Project goals

The project combines embedded systems, data engineering and data science.

## Project status

🚧 Project under active development.

## Architecture

```text
ESP32
  ↓
FastAPI
  ↓
PostgreSQL
  ↓
dbt
  ↓
Analytics / ML
  ↓
Dashboard