from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()


def load_data():
    try:
        with open('../patient.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []
    
def save_data(data):
    with open('../patient.json', 'w') as file:
        json.dump(data, file)


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Enter Patient ID", examples=["P001"])]
    name: Annotated[str, Field(..., description="Enter Patient Name", examples=["John Doe"])]
    City: Annotated[str, Field(..., description="Enter City Name", examples=["Kolkata"])]
    age: Annotated[int, Field(..., gt=0, description="Enter Patient's age")]
    gender: Annotated[Literal["Male", "Female", "Others"], Field(..., description="Enter Patient's gender")]
    height: Annotated[float, Field(..., gt=0, description="Enter Patient's height in mtrs")]
    weight: Annotated[float, Field(..., gt=0, description="Enter Patient's weight in kg")]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"


@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient ID already exists.")
    data[patient.id] = patient.model_dump(exclude= ['id'])
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})
