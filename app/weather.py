import os
import httpx
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# retrieve api key using os.getenv
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


async def fetch_weather(city_name: str, units: str = 'metric'):
    
    # search parameters sent to the API
    params ={
        'q': city_name,
        'appid': API_KEY,
        'units': units
    }
    # create an asynchronous HTTP client
    async with httpx.AsyncClient() as client:

        # make a GET request to the OpenWeather API
        response = await client.get(BASE_URL, params=params)

        #if error occurs, raise an exception
        response.raise_for_status()
        
        # convert the JSON response to a Python dictionary
        data = response.json()
        
        # extract relevant information from the response
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }