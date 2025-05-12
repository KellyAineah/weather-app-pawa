from fastapi import FastAPI, Query, HTTPException
from app.weather import fetch_weather
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
    
