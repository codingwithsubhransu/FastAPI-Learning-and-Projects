from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact details are required for patients over 60 years old.")
        else:
            return model
        

def update_patient_details(patient: Patient):
    print(f"Updating details for patient: {patient.name}")


patient_info = {
    "name": "John Doe",
    "age": 65,
    "email": "johndoe@example.com",
    "weight": 70.5,
    "married": True,
    "allergies": ["penicillin"],
    "contact_details": {
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA",
        "emergency": "987-654-3210"
    }
}

patient1 = Patient(**patient_info)
update_patient_details(patient1)
