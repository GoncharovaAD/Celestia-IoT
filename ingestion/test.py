import psycopg
from dotenv import load_dotenv
import os

load_dotenv(override=True)

password = os.getenv("SUPABASE_DB_PASSWORD")

try:
    with psycopg.connect(
        host="aws-1-eu-west-1.pooler.supabase.com",
        port=5432,
        dbname="postgres",
        user="postgres.chcsiqxwoqpcmtjsemli",
        password=password,
    ) as conn:
        print("SUCCESS: connected to Supabase!")

except Exception as e:
    print("ERROR:")
    print(e)