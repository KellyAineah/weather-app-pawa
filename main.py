from fastapi import FastAPI, Query, HTTPException
from app.weather import fetch_weather, fetch_forecast
from fastapi.middleware.cors import CORSMiddleware
import asyncio

#initialize our application
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "https://weather-app-pawa-frontend-dxdn.vercel.app",  # Vercel frontend
        
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Root endpoint to check if the API is working
@app.get("/")
def read_root():
    return {
        "message": "Weather API is working!",
        "test_endpoints": {
            "current_weather": {
                "url": "https://weather-app-pawa.onrender.com/weather?city_name=Nairobi&units=metric",
                "instructions": "Replace 'Nairobi' with any city and optionally change units to 'imperial'"
            },
            "3_day_forecast": {
                "url": "https://weather-app-pawa.onrender.com/forecast?city_name=Nairobi&units=metric",
                "instructions": "Replace 'Nairobi' with any city and optionally change units to 'imperial'"
            }
        },
        "documentation": "See GitHub README for full API specifications"
    }

# Endpoint to fetch weather data
@app.get('/weather')
async def get_weather(city_name: str = Query(..., description="Name of the city to fetch weather for"),
units: str = Query('metric', description="Units of measurement (metric, imperial)")):
    try:
        data = await fetch_weather(city_name=city_name, units=units)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Endpoint to fetch forecast data
@app.get("/forecast")
async def get_forecast(
    city_name: str = Query(..., description="City to fetch 3-day forecast for"),
    units: str = Query("metric", description="Units of measurement: metric or imperial")
):
    try:
        data = await fetch_forecast(city_name=city_name, units=units)
        return data
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))