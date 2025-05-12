# Weather Application 

A modern, asynchronous FastAPI backend that fetches real-time weather data and 3-day forecasts using the OpenWeatherMap API.

## Overview
This weather application lets users retrieve current weather conditions and a 3-day forecast for any city in the world. Built using Python’s FastAPI and powered by asynchronous HTTP requests, it’s designed for performance and scalability.

## Features
  Asynchronous architecture using httpx for non-blocking requests

 City-based weather lookup

 Current weather + 3-day forecast (with 3-hour intervals)

 Environment variable configuration (via .env)

 Testable with pytest and HTTP client mocks

 Supports metric and imperial units

## Project Structure

weather-application/
├── app/
│   ├── __init__.py
│   └── weather.py          # Logic to interact with OpenWeatherMap API
├── main.py                 # FastAPI app entry point
├── tests/
│   └── test_main.py        # API endpoint tests
├── .env                    # API keys and config
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

## Installation

### 1. Clone the repository

git clone https://github.com/your-username/weather-application.git
cd weather-application

### 2. Set up a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add environment variables
Create a .env file in the root directory:


OPENWEATHER_API_KEY=your_openweathermap_api_key

## Usage

### Run the application

uvicorn main:app --reload
Visit: http://localhost:8000

## API Endpoints

### GET /
Health check endpoint.

Response:

json
Copy
Edit
{
  "message": "Weather API is working!"
}
### GET /weather
Retrieve current weather for a city.

Query Parameters:

city_name (required)

units: metric or imperial (default: metric)

Example:

/weather?city_name=Nairobi&units=metric

Response:

{
  "location": "Nairobi, KE",
  "temperature": 25.3,
  "description": "clear sky",
  "icon": "01d",
  "humidity": 60,
  "wind_speed": 3.1
}

### GET /forecast

Retrieve 3-day forecast with 3-hour intervals.

Query Parameters:

city_name (required)

units: metric or imperial (default: metric)

Response:

{
  "location": "Nairobi, KE",
  "forecast": [
    {
      "datetime": "2025-05-13 00:00:00",
      "temperature": 24.5,
      "description": "light rain",
      "icon": "10d",
      "humidity": 65,
      "wind_speed": 4.0
    },
    ...
  ]
}

## Testing

export PYTHONPATH=$(pwd) && pytest -v
Tests are written using pytest and simulate FastAPI endpoints using HTTP clients. Make sure your .env file is populated before running tests.

## Tech Stack

FastAPI – Web framework

httpx – Async HTTP client

python-dotenv – Load environment variables

pytest / pytest-asyncio – Testing

OpenWeatherMap API – Weather data source

## Contributing
Fork the repository

Create a new branch (git checkout -b feature-xyz)

Commit your changes

Push to your fork and submit a Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or collaboration:

Developer: Kelly Aineah Wanyama

Email: kellyainea99@gmail.com

GitHub: @KellyAineah