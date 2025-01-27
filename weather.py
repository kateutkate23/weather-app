import requests
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


def get_lat_lon(city_name, state_code, country_code, api_key):
    data = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q='
        f'{city_name},{state_code},{country_code}&appid={api_key}'
    ).json()[0]
    lat, lon = data.get('lat'), data.get('lon')

    return lat, lon


def get_current_weather(lat, lon, api_key):
    data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    ).json()
    weather = WeatherData(
        main=data.get('weather')[0].get('main'),
        description=data.get('weather')[0].get('description'),
        icon=data.get('weather')[0].get('icon'),
        temperature=int(data.get('main').get('temp'))
    )

    return weather


def main(city_name, state_code, country_code):
    lat, lon = get_lat_lon(city_name, state_code, country_code, api_key)
    weather = get_current_weather(lat, lon, api_key)

    return weather
