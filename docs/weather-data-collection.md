# Weather Data Collection

## Overview

The weather ingestion workflow collects current weather observations for Belgrade from the OpenWeather API and stores the original API responses as raw JSON files.

This is the first external data source in the Celestia-IoT data pipeline. The raw data will later be loaded into PostgreSQL and transformed into analytical tables.

```text
OpenWeather API
       ↓
Python ingestion script
       ↓
Raw JSON files
       ↓
PostgreSQL
       ↓
dbt transformations
       ↓
Analytics / ML
```

## What It Does

The weather collection script:

1. Sends a request to the OpenWeather API.
2. Requests the current weather for Belgrade.
3. Validates the HTTP response.
4. Parses the response as JSON.
5. Saves the original API response to the raw data directory.
 
The raw API response is intentionally preserved before any transformation. This allows the original source data to be reprocessed later if the data model changes.

## API

The workflow uses the **OpenWeather Current Weather API**.

The request uses the following parameters:

`q` — city and country code (Belgrade,RS)  
`appid` — OpenWeather API key  
`units` — metric, so temperature is returned in Celsius  
`lang` — response language

The API key is stored in an environment variable and is never committed to the repository.

`OPENWEATHER_API_KEY=your_api_key`

Local execution: API key from `.env`  
GitHub Actions: API key from GitHub Secrets

## Collection Frequency

The workflow is scheduled to run four times per day. 

Each execution creates a new raw JSON file containing the weather observation collected at that time.

Hourly collection provides a time series that can later be used for:
- weather trend analysis
- data quality monitoring
- correlation with local sensor measurements
- observation/visibility analysis
- machine learning experiments

### What the Script Requests

The script currently requests the following information from OpenWeather:
- current temperature
- feels-like temperature
- atmospheric pressure
- humidity
- cloudiness
- wind speed
- visibility
- weather condition
- weather description
- geographic coordinates
- API observation timestamp

The complete API response is stored in its original JSON structure.

## Raw Data Storage

Raw weather data is stored in:
`data/raw/weather/`

The `raw` directory contains data exactly as it was received from the external API, without analytical transformations.

## JSON Filename Convention

Each JSON file is named using the UTC timestamp when the data was collected.

Format: `YYYYMMDD_HHMMSS.json`  

Example: `20260915_110000.json`

This corresponds to: `2026-09-15 11:00:00 UTC`

Using timestamps in filenames makes the files easy to sort chronologically and avoids filename collisions.

## API Request Failure

The script checks the HTTP response before saving the data.

If the API request fails, the script raises an error instead of saving an invalid response as weather data.

For example: `response.raise_for_status()`

This allows GitHub Actions to detect the failed workflow execution.

Possible causes of failure include:
- invalid API key
- API rate limit
- network failure
- unavailable API
- invalid request parameters

Failed executions should be investigated using the GitHub Actions logs.

### Running the Script Manually

Make sure the virtual environment is activated and the required dependencies are installed.

From the project root: `.venv\Scripts\Activate.ps1`

Then run: `python ingestion/weather.py`

A successful execution should create a new JSON file in: `data/raw/weather/`

For example: `Saved: data/raw/weather/20260915_110000.json`

You can then open the JSON file and inspect the raw API response.

## GitHub Actions

The weather collection workflow can also be executed automatically using GitHub Actions.

To check the workflow status:

1. Open the Celestia-IoT repository on GitHub.
2. Go to the Actions tab.
3. Select the weather data collection workflow.
4. Open the latest workflow run.
5. Click the relevant job.
6. Expand the individual steps to inspect the logs.

A successful run should show a completed workflow and a newly generated weather data file.

If the workflow fails, the logs can be used to identify the problem, for example:
- missing environment variable 
- invalid API key 
- Python dependency error 
- HTTP/API error 
- file system error 
