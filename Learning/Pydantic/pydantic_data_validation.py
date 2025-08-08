from pydantic import BaseModel, AnyUrl, EmailStr, Field
from typing import Optional, List, Dict, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(max_length= 50,title="Name of the patient", description="Name of the patient, max length 50 characters", examples=['Subhransu', "Chintu"])]
    age: Annotated[int, Field(gt=0, lt=120, description="Age must be between 0 and 120 years", examples=[24, 30])]
    # email: EmailStr   -> Not working due to some issue
    weight: Annotated[float, Field(gt=0, description="Weight must be greater than 0", examples=[65.5, 70.0], strict=True)]
    married: Annotated[bool, Field(default=False, description="Marital status of the patient")]
    allergies: Annotated[Optional[List[str]], Field(default=None, description="List of allergies the patient has")]
    contact_details: Dict[str, str]
    linkedin_url: AnyUrl


def insert_data(patient: Patient):
    print(f"{patient.name}, {patient.age}")


patient_info = {"name": "Subhransu", "age": 24 ,"weight": 65.5, "contact_details": {"email": "abc@gmail.com"}, "linkedin_url": "https://linkedin.com"}
Patient1 = Patient(**patient_info)
insert_data(Patient1)