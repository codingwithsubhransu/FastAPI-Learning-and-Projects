

'''
    So we need pydantic for two reason described in below code snippet.
    1. As, python does not have any build in python type validation system. So pydantic is required to validate the data.
    2. To convert the data into a specific format.

    So as you see below the code snippet I have written doen't have any type validation system.
    So, if I pass a string instead of an integer for age, it will not raise an error.
    This is a problem because we want to ensure that the data we are working with is of the correct type.
    Pydantic solves this problem by providing a way to define data models with type annotations.
    This decreases various manual work and makes the code more readable and maintainable.
'''

def add_patient(name: str, age: int):
    if type(name) is not str or type(age) is not int:
        raise TypeError("Invalid data types provided.")
    else:
        print(f"Adding patient: {name}, Age: {age}")
        print("Added to the database.")

add_patient("John Doe", 30)