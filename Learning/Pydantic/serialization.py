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


temp = patient1.model_dump(exclude={'address': ['state']})
print(temp, type(temp))

temp = patient1.model_dump(exclude_unset= True) # exclude_unset is used to prevent export of undefined data
print(temp)