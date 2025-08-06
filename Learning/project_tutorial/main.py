from fastapi import FastAPI, Path, HTTPException, Query
import json

def load_json():
    with open('../patient.json', 'r') as f:
        data = json.load(f)
    return data

app = FastAPI()

@app.get('/')
def hello():
    return {'message': 'Patient management system API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional api to manage your patients and their records.'}

@app.get('/view')
def view():
    data = load_json()
    return {"data": data}

# @app.get('/patient/{patient_id}')
# def get_patient(patient_id: str):
#     data = load_json()
#     if patient_id in data:
#         return {"patient": data[patient_id]}
#     else:
#         return {'Error': "Patient not found."}

'''By using Path Params'''
# @app.get('/patient/{patient_id}')
# def get_patient(patient_id: str = Path(..., description= "Enter Patient Id", example= "P001")):
#     data = load_json()
#     if patient_id in data:
#         return {"patient": data[patient_id]}
#     else:
#         return {'Error': "Patient not found."}

'''By Using HTTPException'''
@app.get('/patient/{patient_id}')
def get_patient(patient_id: str = Path(..., description="Enter Patient Id", example="P001")):
    data = load_json()
    if patient_id in data:
        return {"patient": data[patient_id]}
    raise HTTPException(status_code=404, detail="Patient not found.")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight, age or bmi"), order: str = Query("asc", description= "sort n asc and desc order")):
    valid_sort_fields = ['height', 'weight', 'age', 'bmi']
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Choose from {valid_sort_fields}.")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'.")
    
    data = load_json()
    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse=(order == 'desc'))
    return {"sorted_data": sorted_data}