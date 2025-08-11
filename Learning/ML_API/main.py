from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd 


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]



#pydantic model
class UserInput(BaseModel):
    age: Annotated[int, Field(..., description="Age of the user in years", gt= 0, le=120)]
    weight: Annotated[float, Field(..., description="Weight of the user in kilograms", gt=0)]
    height: Annotated[float, Field(..., description="Height of the user in centimeters")]
    income_lpa: Annotated[float, Field(..., description="Income of the user in lakhs per annum")]
    smoker: Annotated[bool, Field(..., description="Smoking status of the user")]
    city: Annotated[str, Field(..., description="City of residence of the user")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        height_m = self.height / 100
        return self.weight / (height_m ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 65:
            return "middle_aged"
        else:
            return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> str:
        if self.city in tier_1_cities:
            return "tier_1"
        elif self.city in tier_2_cities:
            return "tier_2"
        else:
            return "tier_3"
    

@app.post("/predict")
def predict_premium(data: UserInput):
    input_data = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_data)[0]
    return JSONResponse(status_code= 200 ,content={"predicted_category": prediction})    