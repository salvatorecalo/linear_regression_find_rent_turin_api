from fastapi import FastAPI
from pydantic import BaseModel
from shapely.geometry import shape
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class AreaGeoJSON(BaseModel):
    geometry: dict 

@app.post("/predict-rent/")
def predict_rent(area: AreaGeoJSON):
    polygon = shape(area.geometry)

    area_kmq = polygon.area * 100  # semplificato

    prediction = {
        "estimated_rent_per_m2": 14.2,
        "area_kmq": area_kmq,
        "total_rent_estimate": area_kmq * 1000000 * 14.2 / 10000  # approssimativo
    }

    return prediction
