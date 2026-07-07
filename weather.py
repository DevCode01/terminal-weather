#!/usr/bin/env python3
"""Terminal Weather - Weather forecast in your terminal."""
import json
import urllib.request
import sys

def get_weather(city):
    print(f'Weather for: {city}')
    print('=' * 40)
    print('[TODO: integrate with wttr.in or OpenWeatherMap API]')
    print('Run: curl wttr.in/' + city)

if __name__ == '__main__':
    city = sys.argv[1] if len(sys.argv) > 1 else 'Paris'
    get_weather(city)
