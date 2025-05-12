import os
import httpx
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# retrieve api key using os.getenv
API_KEY = os.getenv("OPENWEATHER_API_KEY")

WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Function to get latitude and longitude based on city name
async def get_coordinates(city_name: str):
    params = {
        'q': city_name,
        'limit': 1,
        'appid': API_KEY,
    }

    try:
        # Create an asynchronous HTTP client
        async with httpx.AsyncClient() as client:
            # Make a GET request to the geocoding API
            response = await client.get(GEOCODING_URL, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors

            # Convert response JSON to Python dictionary
            data = response.json()

            # If city not found, raise error
            if not data:
                raise Exception(f"City '{city_name}' not found.")

            # Return extracted latitude, longitude, city, and country
            return {
                'lat': data[0]['lat'],
                'lon': data[0]['lon'],
                'city': data[0]['name'],
                'country': data[0]['country']
            }

    except httpx.HTTPStatusError as http_err:
        raise Exception(f"Geocoding API error: {http_err.response.text}")
    except Exception as err:
        raise Exception(f"Error fetching coordinates: {str(err)}")


# Function to fetch weather data using coordinates
async def fetch_weather(city_name: str, units: str = 'metric'):
    try:
        # Get coordinates from city name
        coords = await get_coordinates(city_name)

        # Search parameters sent to the weather API
        params = {
            'lat': coords['lat'],
            'lon': coords['lon'],
            'units': units,
            'appid': API_KEY,
        }

        # Create an asynchronous HTTP client
        async with httpx.AsyncClient() as client:
            # Make a GET request to the weather API
            response = await client.get(WEATHER_BASE_URL, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors

            # Convert response JSON to Python dictionary
            data = response.json()

            # Extract and return relevant weather information
            return {
                'location': f"{coords['city']}, {coords['country']}",
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }
    # Handle exceptions
    except httpx.HTTPStatusError as http_err:
        raise Exception(f"Weather API error: {http_err.response.text}")
    except Exception as err:
        raise Exception(f"Error fetching weather: {str(err)}")
    

async def fetch_forecast(city_name: str, units: str = 'metric'):
    try:
            # Get coordinates from city name
            coords = await get_coordinates(city_name)

            # Search parameters sent to the weather API
            params = {
                'lat': coords['lat'],
                'lon': coords['lon'],
                'units': units,
                'appid': API_KEY,
            }

            # Create an asynchronous HTTP client
            async with httpx.AsyncClient() as client:
                # Make a GET request to the weather API
                response = await client.get(FORECAST_URL, params=params)
                response.raise_for_status()  # Raise exception for HTTP errors

                # Convert response JSON to Python dictionary
                data = response.json()

                #slice the data to get the next 3 days (24 entries = 3days @ 3-hour intervals)
                sliced_forecast = data['list'][:24]

                #structure forecast data
                 
                forecast_data = []
                # Loop through the sliced forecast data and extract relevant information
                for entry in sliced_forecast:
                    forecast_data.append({
                        'datetime': entry['dt_txt'],
                        'temperature': entry['main']['temp'],
                        'description': entry['weather'][0]['description'],
                        'icon': entry['weather'][0]['icon'],
                        'humidity': entry['main']['humidity'],
                        'wind_speed': entry['wind']['speed'],
                    })

                # Return the forecast data
                return {
                    'location': f"{coords['city']}, {coords['country']}",
                    'forecast': forecast_data,
                }
        ## Handle exceptions
    except httpx.HTTPStatusError as http_err:
            raise Exception(f"Forecast API error: {http_err.response.text}")    
    except Exception as err:
            raise Exception(f"Error fetching forecast: {str(err)}")    

        