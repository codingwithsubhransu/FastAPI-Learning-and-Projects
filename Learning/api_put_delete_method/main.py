from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
from fastapi.responses import JSONResponse

def load_data():
    with open('../patient.json', 'r') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open('../patient.json', 'w') as f:
        json.dump(data, f)

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Enter Patient ID", examples=["P001"])]
    name: Annotated[str, Field(..., description="Enter Patient name", examples=["John Doe"])]
    city: Annotated[str, Field(..., description="Enter your city name", examples=["Kolkata"])]
    age: Annotated[int, Field(..., description="Enter your age", gt=0)]
    gender: Annotated[Literal["Male", "Female", "Other"], Field(..., description="Enter your gender")]
    height: Annotated[float, Field(..., description="Enter your height in cm", gt=0)]
    weight: Annotated[float, Field(..., description="Enter your weight in kg", gt=0)]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2
    
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
        
'''Get data from the database'''
@app.get('/')
def greetings():
    return JSONResponse(status_code=200, content={"message": "Welcome to the Patient API endpoint"})


'''Update or edit patients'''

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal["Male", "Female", "Other"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

@app.put('/edit/{id}')
def update_patient(id: str, patient_update: PatientUpdate):
    data = load_data()
    if id not in data:
        raise HTTPException(status_code=404, detail="Patient not found.")
    existing_patient_info = data[id]
    updated_patient_info = patient_update.model_dump(exclude_unset= True)
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info['id'] = id
    patient_pydantic_object = Patient(**existing_patient_info)
    existing_patient_info = patient_pydantic_object.model_dump(exclude= 'id')
    data[id] = existing_patient_info

    save_data(data)
    return JSONResponse(status_code= 201, detail= {"message": "Patient Updated Successfully"})


'''Delete data'''

@app.delete('/delete/{id}')
def delete_patient(id: str):
    data = load_data()
    if id not in data:
        raise HTTPException(status_code= 404, detail= {"message": "Patient not found"})
    del data[id]
    save_data(data)
    return JSONResponse(status_code= 201, content= {"message": "Content deleted successfully"})

