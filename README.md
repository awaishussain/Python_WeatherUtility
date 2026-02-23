# Python Weather Utility 🌤️

A simple Python application that fetches and displays real-time weather information for any city using the OpenWeatherMap API.

## Features

- Secure API key management using environment variables (.env file) 
- Get current weather for any city worldwide
- Displays temperature in Celsius
- Provides weather descriptions (clear sky, rain, etc.)
- Easy-to-use command-line interface

## Prerequisites

Before running this project, make sure you have:

- Python 3.x installed
- An API key from [OpenWeatherMap](https://openweathermap.org/api) (free tier available)

## Installation
pip install requests

## Setup environment variables
Create a `.env` file in the root directory and add your API key:
```env   API_KEY=your_actual_api_key_here
Get your free API key from OpenWeatherMap

## Setup API KEY
Open Get_Data.py and replace "YOUR_API_KEY_HERE" with your actual API key

## Run the script

python Display_Weather.py

## Enter city name and the program will display:

Current temperature
Weather conditions
Humidity level

## How it works
Display_Weather.py takes a city name as input from the user
It calls functions from Get_Data.py to fetch weather data
Get_Data.py makes an API request to OpenWeatherMap
The data is processed and displayed in a user-friendly format

## Author:
Syed Awais Hussain