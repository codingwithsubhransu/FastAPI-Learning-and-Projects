from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_dict = {'city': "Puri", "state": "Odisha", "pin": "752011"}
address = Address(**address_dict)
patient_dict = {"name": "Subhransu", "age": 25, "gender": "Male", "address": address}
patient1 = Patient(**patient_dict)
print(patient1)

#Features

# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use vitals in multiple models (e.g., Patient MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically-no extra work needed