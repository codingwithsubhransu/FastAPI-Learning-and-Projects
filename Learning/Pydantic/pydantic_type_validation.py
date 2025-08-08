from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False # Setting the default value
    allergies: Optional[List[str]] = None  #Process to set optional value
    contact_details: Dict[str, str]

def insert_patient(patient: Patient):
    # Simulate inserting a patient into a database
    print(f"Inserting patient: {patient.name}, Age: {patient.age}, contact: {patient.contact_details}, allergies: {patient.allergies}, married :{patient.married}")


patient_info = {"name": "John Doe", "age": 30, "weight": 70.5, "contact_details": {'email': 'abc@gmail.com', 'phone': '2305096'}}

Patient1 = Patient(**patient_info)
insert_patient(Patient1)