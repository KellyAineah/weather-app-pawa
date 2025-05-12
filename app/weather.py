import os
import httpx
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# retrieve api key using os.getenv
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

