import json
import os
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

import psycopg
from psycopg.types.json import Jsonb


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY is not set")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Belgrade,RS",
    "appid": API_KEY,
    "units": "metric",
    "lang": "en",
}

response = requests.get(url, params=params, timeout=10)

response.raise_for_status()

data = response.json()

collected_at = datetime.now(timezone.utc)


# Collecting data into PostrgreSQL (in future)
POSTGRES_HOST = os.getenv("POSTGRES_HOST")

if POSTGRES_HOST:
    conn = psycopg.connect(
        host=POSTGRES_HOST,
        port=os.getenv("POSTGRES_PORT", "5432"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO weather_raw (
                    collected_at,
                    source,
                    payload
                )
                VALUES (%s, %s, %s)
                """,
                (
                    collected_at,
                    "openweather",
                    Jsonb(data),
                ),
            )

    conn.close()

# Saving JSON

if os.getenv("GITHUB_ACTIONS") == "true":
    output_dir = Path("data/samples/weather")
else:
    output_dir = Path("data/raw/weather")
    
output_dir.mkdir(parents=True, exist_ok=True)

filename = collected_at.strftime("%Y%m%d_%H%M%S.json")

output_file = output_dir / filename

with output_file.open("w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print(f"Saved: {output_file}")