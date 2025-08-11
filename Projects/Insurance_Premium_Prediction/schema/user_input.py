from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):
    age: Annotated[int, Field(..., description="Age of the user in years", gt= 0, le=120)]
    weight: Annotated[float, Field(..., description="Weight of the user in kilograms", gt=0)]
    height: Annotated[float, Field(..., description="Height of the user in centimeters")]
    income_lpa: Annotated[float, Field(..., description="Income of the user in lakhs per annum")]
    smoker: Annotated[bool, Field(..., description="Smoking status of the user")]
    city: Annotated[str, Field(..., description="City of residence of the user")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]
    

    @field_validator('city')
    @classmethod
    def normalize_city(cls, v:str) -> str:
        return v.strip().title()
    
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