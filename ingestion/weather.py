import json
import os
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

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

timestamp = datetime.now(timezone.utc)

output_dir = Path("data/raw/weather")
output_dir.mkdir(parents=True, exist_ok=True)

filename = timestamp.strftime("%Y%m%d_%H%M%S.json")

output_file = output_dir / filename

with output_file.open("w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print(f"Saved: {output_file}")