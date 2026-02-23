import requests
import os
from dotenv import load_dotenv
load_dotenv()


class WeatherClass:
    def getWeatherData(self, cityname):
        params = {
            "q": cityname,
            "appid": os.getenv('API_KEY'),
            "units": "metric"
        }
        
        response = requests.get(os.getenv('BASE_URL'), params=params)
        if response.status_code != 200:
            raise Exception("City not found or API error.")
            
        data = response.json()
        compData = {
            "main": data["main"]["temp"],
            "FeelData": data["main"]["feels_like"],
            "desc": data["weather"][0]["description"]
        }
        return compData
