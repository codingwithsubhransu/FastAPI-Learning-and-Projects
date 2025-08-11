import pickle
import pandas as pd 



with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

class_labels = model.classes_.tolist()
# MLFlow
MODEL_VERSION = '1.0.0'


def predict_output(user_input: dict) -> str:
    input_data = pd.DataFrame([user_input])
    predicted_class = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))
    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }