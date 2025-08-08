# Why use Pydantic
### So we need pydantic for two reason described in below code snippet.
    1. As, python does not have any build in python type validation system. So pydantic is required to validate the data.

    2. To convert the data into a specific format.

So as you see below the code snippet I have written doen't have any type validation system.

So, if I pass a string instead of an integer for age, it will not raise an error.
    
This is a problem because we want to ensure that the data we are working with is of the correct type.

Pydantic solves this problem by providing a way to define data models with type annotations.
    
This decreases various manual work and makes the code more readable and maintainable.


## Steps to create validate using Pydantic

***Step 1.*** 
Define Pydantic model/class that represents the ideal schema of the data.

***Step2.***
Instantiate the model with raw input data.

***Step3.***
Pass the validated model object to functions or use it throughout your codebase.