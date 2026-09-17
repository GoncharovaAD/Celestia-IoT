CREATE TABLE weather_observations AS
SELECT
    id,
    collected_at,

    to_timestamp((payload->>'dt')::bigint) AS observed_at,

    payload->>'name' AS city,

    (payload->'coord'->>'lat')::numeric AS latitude,
    (payload->'coord'->>'lon')::numeric AS longitude,

    (payload->'main'->>'temp')::numeric AS temperature_c,
    (payload->'main'->>'feels_like')::numeric AS feels_like_c,
    (payload->'main'->>'humidity')::integer AS humidity_pct,
    (payload->'main'->>'pressure')::integer AS pressure_hpa,

    (payload->'clouds'->>'all')::integer AS cloudiness_pct,

    (payload->'wind'->>'speed')::numeric AS wind_speed_ms,

    payload->'weather'->0->>'main' AS weather_main,
    payload->'weather'->0->>'description' AS weather_description

FROM weather_raw;