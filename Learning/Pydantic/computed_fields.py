from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
def update_patient_details(patient: Patient):
    print(f"Updating details for patient: {patient.name}")
    print(f"Patient's BMI: {patient.bmi}")

patient_info= {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "weight": 70.5,
    "height": 1.75,
    "married": True,
    "allergies": ["penicillin"],
    "contact_details": {
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
    }
}

patient1 = Patient(**patient_info)
update_patient_details(patient1)