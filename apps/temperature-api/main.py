from random import uniform

from fastapi import FastAPI

app = FastAPI()


def _get_response():
    return {
        "value": round(uniform(10.0, 28.0), 1),
        "unit": "°C",
        "timestamp": "2025-06-08T20:57:13.064632Z",
        "location": "Living Room",
        "status": "inactive",
        "sensor_id": "1",
        "sensor_type": "temperature",
        "description": "Living Room Temperature",
    }

@app.get("/temperature")
async def get_temperature(location: str = "") -> dict:
    return _get_response()

@app.get("/temperature/{id_}")
async def get_temperature(id_: int = 0) -> dict:
    return _get_response()


