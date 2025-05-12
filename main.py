from fastapi import FastAPI, Query, HTTPException
from app.weather import fetch_weather, fetch_forecast
import asyncio

#initialize our application
app = FastAPI()

#Root endpoint to check if the API is working
@app.get("/")
def read_root():
    return {'message': 'Weather Api is working!'}

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