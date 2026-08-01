#!/usr/bin/env python3
# Terminal weather report using the free wttr.in service (no API key).
import argparse
import json
import urllib.request

BASE = "https://wttr.in/{}?format=j1"


def fetch(city):
    url = BASE.format(urllib.parse.quote(city))
    with urllib.request.urlopen(url, timeout=15) as resp:
        return json.load(resp)


def print_current(data):
    current = data["current_condition"][0]
    area = data["nearest_area"][0]
    print(f"=== {area['areaName'][0]['value']}, {area['country'][0]['value']} ===")
    print(f"Condition:  {current['weatherDesc'][0]['value']}")
    print(f"Temp:       {current['temp_C']} C / {current['temp_F']} F")
    print(f"Feels like: {current['FeelsLikeC']} C")
    print(f"Wind:       {current['windspeedKmph']} km/h ({current['winddir16Point']})")
    print(f"Humidity:   {current['humidity']}%")
    print(f"Visibility: {current['visibility']} km")


def print_forecast(data):
    print()
    print("3-day forecast:")
    for day in data["weather"]:
        print(
            f"  {day['date']}: min {day['mintempC']}C "
            f"/ max {day['maxtempC']}C - "
            f"{day['hourly'][4]['weatherDesc'][0]['value']}"
        )


def main():
    parser = argparse.ArgumentParser(description="Terminal weather via wttr.in")
    parser.add_argument("city", help="City name (e.g. Paris)")
    args = parser.parse_args()

    try:
        data = fetch(args.city)
    except Exception as e:
        print(f"Error fetching weather: {e}", file=sys.stderr)
        return 1

    print_current(data)
    print_forecast(data)
    return 0


if __name__ == "__main__":
    import sys
    import urllib.parse
    raise SystemExit(main())
