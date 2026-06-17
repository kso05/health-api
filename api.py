from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd

from .health import Health
from .data import load_json, save_json

app = FastAPI()

# What the client sends -- POST /records
class RecordIn(BaseModel):
    name: str
    weight_kg: float
    height_m: float

# What the server returns -- GET /records and POST /records
class RecordOut(BaseModel):
    name: str
    weight_kg: float
    height_m: float
    bmi: float
    category: str
    ideal_weight: float

# GET / -- no request body, no response_model needed
@app.get("/")
def health_check():
    return {
        "status": "ok",
        "app": "Health API"
    }

# GET /records -- returns all records from the database
@app.get("/records", response_model=List[RecordOut])
def get_records():

    records = load_json()

    result = []

    for record in records:
        result.append(
            RecordOut(
                name=record.name,
                weight_kg=record.weight_kg,
                height_m=record.height_m,
                bmi=record.bmi,
                category=record.get_category(),
                ideal_weight=record.get_ideal_weight()
            )
        )

    return result

# POST /records -- RecordIn comes in, RecordOut goes back
@app.post("/records", response_model=RecordOut, status_code=201)
def create_record(record: RecordIn):

    # Create Health object using existing class
    health_record = Health(
        record.name,
        record.weight_kg,
        record.height_m
    )

    # Save to JSON file using existing function
    save_json([health_record])

    # Return shaped response
    return RecordOut(
        name=health_record.name,
        weight_kg=health_record.weight_kg,
        height_m=health_record.height_m,
        bmi=health_record.bmi,
        category=health_record.get_category(),
        ideal_weight=health_record.get_ideal_weight()
    )








