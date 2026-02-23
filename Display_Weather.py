from Get_Data import WeatherClass
from dotenv import load_dotenv
load_dotenv()


def ShowWeather():
        service = WeatherClass()
        
        while True:
            city = input("\nEnter city name (or type 'quit' to exit): ")

            if city.lower() == "quit":
                print("Exiting Weather App.")
                break

            try:
                weather = service.getWeatherData(city)

                print("Weather in:" + city)
                print(f"Temperature: {weather['main']} °C")
                print(f"Feels Like: {weather['FeelData']} °C")
                print(f"Description: {weather['desc']}")

            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    ShowWeather()
