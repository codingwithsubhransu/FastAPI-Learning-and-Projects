from fastapi import FastAPI
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