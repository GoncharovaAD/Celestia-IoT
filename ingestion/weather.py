import os
from datetime import datetime, timezone

import psycopg
import requests
from dotenv import load_dotenv
from psycopg.types.json import Jsonb

load_dotenv(override=True)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY is not set")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")


# -------------------------
# Get weather from API
# -------------------------
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


# -------------------------
# Save to PostgreSQL
# -------------------------
with psycopg.connect(DATABASE_URL) as conn:
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

print(f"Weather data saved: {collected_at.isoformat()}")