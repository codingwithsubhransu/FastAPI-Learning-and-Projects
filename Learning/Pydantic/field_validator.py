from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str):
        valid_domain = ["hdfc.com", "icici.com"]
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError(f"Email domain '{domain_name}' is not allowed. Allowed domains: {valid_domain}")
        return value
    
    @field_validator("name")
    @classmethod
    def transform_name(cls, value: str):
        return value.title()
    
    @field_validator("age", mode= "after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Invalid age. Age must be between 0 and 100.")


def update_patient_details(patient: Patient):
    print(f"Updating details for patient: {patient.name}")


patient_info = {"name": "John Doe", "age": '30', "email": "john.doe@icici.com", "weight": 70.5, "married": False, "allergies": ["penicillin"], "contact_details": {"phone": "123-456-7890"}}
patient1 = Patient(**patient_info) # validation -> type coercion
update_patient_details(patient1)


'''
Field validator is a decorator that allows you to define custom validation logic for individual fields in a Pydantic model. It can be used to enforce constraints, transform input data, or perform additional checks before the data is processed.

-> It operates in two mode: 
i. before: this mode is used to assign or pass the value before the typecast
ii. after: this mode is used to validate or transform the value after the typecast

'''