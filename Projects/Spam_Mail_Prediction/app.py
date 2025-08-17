from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import Message
from model.prediction import predict_output, MODEL_VERSION, model

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Spam Mail Prediction API"
    }

@app.get("/health")
def health_check():
    return {
        "status": "Ok",
        "version": MODEL_VERSION,
        "model_loaded": model is not None
    }

@app.post("/predict")
def predict(message: Message):
    input_data = [message.message]
    try:
        prediction = predict_output(input_data)
        return JSONResponse(status_code= 200, content= {"prediction": prediction})
    except Exception as e:
        return JSONResponse(status_code= 500, content= {"error": str(e)})