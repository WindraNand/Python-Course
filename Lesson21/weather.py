import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get current weather condition ***")
    
    city = input("\n please enter a city name:\n")
    
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)
    
    weather_data = requests.get(request_url).json()
    
    # pprint(weather_data)
    
    print(f"\nCurrent weather for {weather_data["name"]}\n")
    print(f"\nCurrent temp is {weather_data["main"]["temp"]}\n")
    print(f"\nFeels like {weather_data["main"]["feels_like"]}\n")
    
if __name__ == "__main__":
    get_current_weather()
    